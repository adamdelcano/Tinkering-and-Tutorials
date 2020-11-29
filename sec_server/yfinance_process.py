from datetime import date
from datetime import timedelta

import pandas as pd
import yfinance as yf

def get_history(stock: str, window: int) -> pd.DataFrame:
    """
    Retrieves stock ticker history for the last window of time.

    Given a stock and window, uses yfinance to create a Ticker object and then
    using datetime to get the current date and timedelta == window to get the
    appropriate start/end dates, returns the history of the stock.

    Takes as arguments a string stock which should be an extant stock ticker,
    and an int window which represents a number of days, and returns a pandas
    dataframe.
    """
    stock_obj = yf.Ticker(stock)
    today = date.today()
    # realized as i finished for the day that this doesn't handle date right
    # since it's tracking calendar and not business days, need to fix that
    # probably just using the pandas stuff from last time
    duration = timedelta(days=window)
    starting = today - duration
    return stock_obj.history(start=starting, end=today)


if __name__ == '__main__':
    test = get_history('mrna', 30)
    print(test)
