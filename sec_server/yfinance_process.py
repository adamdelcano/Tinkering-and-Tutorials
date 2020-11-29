from datetime import date

import pandas as pd
import yfinance as yf


async def get_history(stock: str, window: int) -> pd.DataFrame:
    """
    Retrieves stock ticker history for the last window of time.

    Given a stock and window, uses yfinance to create a Ticker object and then
    using datetime to get the current date and timedelta == window to get the
    appropriate start/end dates, returns the history of the stock.

    Takes as arguments a string stock which should be an extant stock ticker,
    and an int window which represents a number of days, and returns a pandas
    dataframe.
    """
    window += 1
    stock_obj = yf.Ticker(stock)
    today = date.today()
    # window + 1 here so that the range is actually len(window)
    starting_point = today - pd.tseries.offsets.BDay(window + 1)
    return stock_obj.history(start=starting_point, end=today)
