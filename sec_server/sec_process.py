import asyncio
import concurrent.futures
from datetime import date
from functools import partial
import logging

import motor.motor_asyncio
import pandas as pd
import yfinance as yf


# This chunk is for the window_forecast endpoint
class Stock:
    """
    Class representing a single stock. Has methods to check and update prices.



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

        prices: initially Nonetype, is filled with dataframe of prices for the
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

    async def _get_yf(
        self,
        beginning: date = None,
        ending: date = None,
    ) -> pd.DataFrame:
        """
        Returns the ticker's prices from yfinance.

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

    async def get_prices(self):
        """
        Public facing method for the class to update without mongodb.
        Calls the _get_yf coroutine and sets self.prices to it
        """
        self.prices = await self._get_yf()

    # NOT YET FUNCTIONAL!
    # TODO: Should evaluate whether this is better done as upsert
    async def mongo_insert(self, df: pd.DataFrame) -> None:
        new_docs = [
            {
                'ticker': self.ticker,
                'date': date,
                'price': price
            }
            # triple list comprehension for style
            for date in df.index for col in df.columns for price in df[col]
        ]

        result = await self.db.insert_many(new_docs, ordered=False)
        logging.info(f'Inserted {len(result.inserted_ids)} docs')

    # TODO: Break this down into individual actions, it's doing too much
    async def check_mongo(self) -> None:
        """
        Queries db about the ticker / dates.

        Builds a pipeline to query, then creates an AsyncIOMotorCursor
        using the pipeline. Then builds a dataframe out of the cursors' to_list
        result, compares it with the date_range, and queries _get_yf for the
        missing dates, starting with the oldest and grabbing the newest.
        It then concatenates them, and uses that to update the prices.
        """
        pipeline = []
        ticker_name = {"$match": {"ticker": self.ticker}}
        dates = {"$match": {"date": {"$in": {self.date_range}}}}
        pipeline.extend(ticker_name, dates)
        cursor = await self.db.aggregate(pipeline)
        documents = await cursor.to_list()
        documents_df = pd.DataFrame(documents)
        missing_dates = self.date_range.difference(documents_df)
        if missing_dates.empty is False:
            new_prices = await self._get_yf(
                missing_dates[0], missing_dates[-1]
            )
            await self.mongo_insert(new_prices)
            full_prices = pd.concat([documents_df, new_prices]).sort_index()

        else:
            full_prices = documents_df
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
    Converts incoming data to dataframe.

    At this time this is an extremely simple function, separated out for the
    purpose of expanding to handle errors.

    Takes a dict as sole parameter, logs it, and then
    converts it into a pandas dataframe, which it returns.
    """
    logging.info(f'Converting {data} to dataframe')
    df = pd.DataFrame(data)
    return df


async def extrapolate(data: dict) -> pd.DataFrame:
    """
    Extrapolates the data, adding new days with appropriate values.

    Extrapolate uses the process function to create a pandas dataframe,
    converts the index to datetime, advances the date until it wouldn't be a
    weekend, appends that non-weekend date as the next blank row at the end
    of the dataframe, then interpolates data to fill the new row. It then
    converts the datetime index back to string and returns the dataframe.
    It logs at each major step for redundance- note that logging is blocking.

    Takes a dict as sole parameter, returns a pd.DataFrame object
    """
    # convert dict to dataframe
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
    import asyncio
    mrna = Stock('mrna', 30)
    # using a pickled dataframe so I'm not a jerk
    # mrna.get_history()
    mrna.prices = pd.read_pickle('./mrna_test_data.pkl')
    print(mrna.prices.iloc[-1])
    asyncio.run(mrna.extrapolate_next_day())
    print(mrna.next_price)
