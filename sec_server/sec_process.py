from datetime import date
import logging

import pandas as pd
import yfinance as yf


class Stock:
    """
    Class representing a single stock

    """

    def __init__(self, ticker: str, window: int) -> None:
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

    async def get_history(self) -> None:
        """ Loads the ticker's history into self.prices. """
        stock_object = yf.Ticker(self.ticker)
        self.prices = stock_object.history(
            start=self.starting_point,
            end=self.today
        )[-self.window:]  # cuts off so that it's just window number of days

    async def extrapolate_next_day(self) -> None:
        """ Using self.prices, extrapolates the next day. """
        self.next_day = pd.date_range(
            start=self.prices.index[-1],
            periods=2, freq='B'
        )[-1]
        df = self.prices
        df.loc[self.next_day] = None
        df = df.interpolate(
            method='spline',
            order=1,
        )
        self.prices = df
        self.next_price = df.iloc[-1]


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
