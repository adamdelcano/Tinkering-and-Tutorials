import asyncio
import concurrent.futures
from datetime import date
from functools import partial
import logging

from aiohttp import web
import motor.motor_asyncio
import pandas as pd
import yfinance as yf


# This chunk is for the window_forecast endpoint
class Stock:
    """
    Class representing a single stock. This object handles the data
    operations of the window_forecast endpoint in views.py. Has methods to
    fetch prices from mongodb, check for missing data, retrieve it from a
    yfinance.Ticker object, compare the two dataframes and then interpolate
    based on the comparison.

    """

    def __init__(
        self,
        ticker: str,
        window: int,
        db: motor.motor_asyncio.AsyncIOMotorCollection
    ) -> None:
        """

        ticker: the name of the ticker, should be string (eg 'AMD')

        window: the number of days to get prices from, should be int (eg 30)

        today: current day (as datetime.date object), used with window to
        calculate actual dates for prices

        starting_point: datetime.date object calculated to be (window + 4)
        business days back from today, this number is padded to make up for
        holidays

        date_range: pandas date_range of business days from starting_point to
        today

        next_day: datetime.date object for the day after the end of date_range,
        which will be either today or tomorrow depending on when it's called

        prices: initially Nonetype, is filled with DataFrame of prices for the
        ticker chosen over the course of date_range

        next_price: the extrapolated price based on prices for the next day of
        the ticker, which will be what the server sends back to requests.
        """
        self.ticker = ticker
        self.window = window
        self.db = db
        self.today = date.today()
        self.starting_point = (
            self.today - pd.tseries.offsets.BDay(window + 4)
        )
        self.date_range = pd.date_range(
            start=self.starting_point, end=self.today, freq='B'
        )
        self.next_day = None  # will contain next day
        self.prices = None  # this will contain the prices
        self.next_price = None  # this will contain extrapolated price

    async def _check_mongo(self) -> pd.DataFrame:
        """
        Queries mongodb for documents matching the ticker in the window.

        Builds a pipeline to query, then creates an AsyncIOMotorCursor
        using the pipeline and builds a DataFrame out of that cursors' to_list
        results.

        Converts the DateTimeIndex to a list b/c it's hashable whereas
        DateTimeIndex isn't.
        """
        pipeline = []
        dates = [date for date in self.date_range]
        ticker_name = {"$match": {"ticker": self.ticker}}
        dates = {"$match": {"date": {"$in": dates}}}
        pipeline.extend([ticker_name, dates])
        cursor = self.db.aggregate(pipeline)
        documents = await cursor.to_list(None)
        documents_df = pd.DataFrame(documents).pivot(
            index='Date', columns='Type', values='Price'
        )
        return documents_df

    async def _get_yf(
        self,
        beginning: date = None,
        ending: date = None,
    ) -> pd.DataFrame:
        """
        Returns the ticker's prices from yfinance.

        Note that yfinance is NOT ASYNCHRONOUS- this function gets the event
        loop and calls yfinance via run_in_executor to handle the I/O-bound
        blocking nature thereof.

        beginning: a datetime.date object representing the first day
        ending: a datetime.date object representing the last day


        """
        if not beginning:
            beginning = self.starting_point
        if not ending:
            ending = self.today
        loop = asyncio.get_running_loop()
        stock_object = await loop.run_in_executor(
            None, partial(yf.Ticker, self.ticker)
        )
        return stock_object.history(
            start=beginning,
            end=ending
        )[-self.window:]  # cuts off so that it's just window number of days

    async def dbless_get_prices(self):
        """
        Public facing method for the class to update in mongod-less use cases.
        Calls the _get_yf coroutine and sets self.prices to it
        """
        self.prices = await self._get_yf()

    async def _mongo_insert(self, df: pd.DataFrame) -> None:
        """
        Processes the dataframe of missing data from Stock._combine_mongo_yf()
        into the desired document format, then inserts it into mongodb. Logs
        the number of inserted docs.
        """

        new_docs = [
            {
                'Ticker': self.ticker,
                'Date': date,
                'Type': col,
                'Price': df.loc[date][col]
            }
            # previous versions hadn't thought through the list comprehension
            for date in df.index for col in df.columns
        ]

        result = await self.db.insert_many(new_docs, ordered=False)
        logging.info(
            f'''Attempted to insert {len(new_docs)} docs.
            Inserted {len(result.inserted_ids)} docs.'''
        )

    async def _combine_mongo_yf(
        self,
        mongo_data: pd.DataFrame,
        yf_data: pd.DataFrame
    ) -> dict:
        """
        Merges the mondogb and yfinance dataframes to form a union of them,
        while de-indexing and re-indexing Date, then produces difference, which
        is a facet showing only the yf_data missing from mongo_data, drops the
        _merge column from each, and returns a dict of the two.

        Calculating missing_prices vs yf_data might seem redundant, but
        it's important to consider that as dates are only being requested in
        windows, scenarios exist where the Venn diagram of mongo_data and
        yf_data are concentric circles with mongo_data inside yf_data. For
        example, if a user requested two weeks of data one week ago, and now
        requests a full month. Thus yf_data could contain substantial
        redundancy. That said, it may be more performant to simply return only
        the full_prices dataframe and handling the faceting/dropping of the
        _merge column in Stock.update_prices().
        """
        mongo_data.reset_index(inplace=True)
        yf_data.reset_index(inplace=True)
        try:
            full_prices = mongo_data.merge(
                yf_data, how='outer', indicator=True
            )
            full_prices.set_index('Date', inplace=True)
            missing_prices = full_prices.loc[
                lambda x: x['_merge'] == 'right_only'
            ]
            full_prices.drop(columns=['_merge'], inplace=True)
            missing_prices.drop(columns=['_merge'], inplace=True)
            return {
                'full_prices': full_prices,
                'missing_prices': missing_prices
            }
        except pd.errors.MergeError:
            logging.warning(f'Merge failed: dumping: {mongo_data.to_string()}')
            logging.warning(f'Merge failed: dumping: {yf_data.to_string()}')

    async def update_prices(self):
        """
        Public-facing method to update the prices using the other
        class methods. Checks mongodb, checks that for missing data,
        retrieves yfinance data for the period between oldest and most recent
        missing dates, uses _combine_mongo_yf to get the full prices and the
        missing prices, and then inserts only the missing prices into mongodb,
        and updates Stock.prices with the full prices.

        """
        logging.info('Checking mongodb')
        mongo_prices = await self._check_mongo()
        missing_dates = None
        if mongo_prices.empty:  # just use yfinance and send it all to mongodb
            logging.info(
                f'No data for {self.ticker} found in mongodb, using yf'
            )
            full_prices = await self._get_yf()

            logging.info('Inserting yf data to mongodb')
            await self._mongo_insert(full_prices)
        else:
            logging.info(f'Checking for missing dates.')
            missing_dates = self.date_range.difference(mongo_prices.index)
        # This section could all be nested under the preceding else but seemed
        # more readable to me as a separate bit of flow control. The initial
        # if statement here checking whether missing dates is a non-empty
        # dataframe is admittedly a bit ugly.
        if missing_dates is not None and not missing_dates.empty:
            logging.info('Acquiring missing dates from yf')
            yf_prices = await self._get_yf(
                missing_dates[0], missing_dates[-1]
            )
            if yf_prices.empty is False:
                price_dict = await self._combine_mongo_yf(
                    mongo_prices, yf_prices
                )
                logging.info('Inserting yf data to mongodb')
                await self._mongo_insert(price_dict['missing_prices'])
                full_prices = price_dict['full_prices']
        else:
            logging.info('Mongo prices were complete')
            full_prices = mongo_prices
        self.prices = full_prices

    async def extrapolate_next_day(self) -> None:
        """
        Using self.prices, extrapolates the next day.

        Uses a date_range to create the next day, adds it to the end of
        self.prices, and populates it with spline-interpolated data

        """
        self.next_day = pd.date_range(
            start=self.prices.index[-1],
            periods=2, freq='B'
        )[-1]
        self.prices.loc[self.next_day] = None
        self.prices = self.prices.interpolate(
            method='spline',
            order=1,
        )
        self.next_price = self.prices.iloc[-1]


# From here on this is for the forecast endpoint
async def process(data: dict) -> pd.DataFrame:
    """
    Converts incoming data to DataFrame.

    At this time this is an extremely simple function, separated out for the
    purpose of expanding to handle errors.

    Takes a dict as sole parameter, logs it, and then
    converts it into a pandas DataFrame, which it returns.
    """
    logging.info(f'Converting {data} to DataFrame')
    df = pd.DataFrame(data)
    return df


async def extrapolate(data: dict) -> pd.DataFrame:
    """
    Extrapolates the data, adding new days with appropriate values.

    Extrapolate uses the process function to create a pandas DataFrame,
    converts the index to datetime, advances the date until it wouldn't be a
    weekend, appends that non-weekend date as the next blank row at the end
    of the DataFrame, then interpolates data to fill the new row. It then
    converts the datetime index back to string and returns the DataFrame.
    It logs at each major step for redundance- note that logging is blocking.

    Takes a dict as sole parameter, returns a pd.DataFrame object
    """
    # convert dict to DataFrame
    df = await process(data)
    # Convert index to datetime, generate next day, append it as blank row
    logging.info('Calculating next day')
    df.index = pd.to_datetime(df.index)
    next_day = pd.date_range(start=df.index[-1], periods=2, freq='B')[-1]
    logging.info('Appending')
    df.loc[next_day] = None
    # Interpolate and put that data in
    df = df.interpolate(
        method='spline',
        order=1,
        limit_direction='forward',
        limit_area='outside'
    )
    # Return index to string, log it, return the value
    df.index = df.index.astype(str)
    logging.info('Extrapolation complete.')
    return df

# Lazy testing
if __name__ == "__main__":
    mrna = Stock('mrna', 30)
    # using a pickled DataFrame so I'm not a jerk
    # mrna.get_history()
    mrna.prices = pd.read_pickle('./mrna_test_data.pkl')
    print(mrna.prices.iloc[-1])
    asyncio.run(mrna.extrapolate_next_day())
    print(mrna.next_price)
