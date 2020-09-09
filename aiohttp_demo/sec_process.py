import os
import pandas as pd
from datetime import datetime

current_directory = str(os.getcwd())


async def log(data, message=''):
    """Logs incoming data in data file, along with optional message"""
    log_file = open((current_directory + '_log.txt'), 'a')
    log_file.write(str(datetime.now()))
    log_file.write(message)
    log_file.write(str(data))
    log_file.write('\n')
    log_file.close()


async def process(data):
    """Converting incoming data to dataframe. Currently in need of expansion
    to handle basic data sanitization and error checking."""
    df = pd.DataFrame(data)
    return df


async def extrapolate(data):
    """Takes the dataframe made by process and adds a new row with
    extrapolated data and returns it."""
    df = await process(data)
    # create next day
    df.index = pd.to_datetime(df.index)  # converts from string to datetime
    next_day = df.index[-1] + pd.Timedelta(1, unit='day')
    # advance until not weekend
    while next_day.weekday() > 4:
        next_day += pd.Timedelta(1, unit='day')
    # append to end of dataframe
    df.loc[next_day] = None
    df.index = df.index.astype(str)  # back to string frm datetime
    # actually interpolate
    df = df.interpolate(limit_area='outside')
    await log(df, 'DataFrame:')
    return df
