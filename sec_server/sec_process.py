# commeted out some imports here because they were used for logging
# import os
# from datetime import datetime
import pandas as pd
import logging
import scipy

# get current directory for logging purposes
#current_directory = str(os.getcwd())


# Deprecated homebrew async logging function because I should have known
# a stdlib logger exists. I may reinstate at some point to try to work a
# basic async logging functionality in
#async def log(data, message=''):
#    """Logs incoming data in data file, along with optional message"""
#    log_file = open((current_directory + '_log.txt'), 'a')
#    log_file.write(str(datetime.now()))
#    log_file.write(message)
#    log_file.write(str(data))
#    log_file.write('\n')
#    log_file.close()


async def process(data):
    """Converting incoming data to dataframe. Currently in need of expansion
    to handle basic data sanitization and error checking, would not be in
    it's own function otherwise."""
    logging.info('Converting %s to dataframe', data)
    df = pd.DataFrame(data)
    return df


async def extrapolate(data):
    """Takes the dataframe made by process and adds a new row with
    extrapolated data and returns it."""
    df = await process(data)
    # create next day
    logging.info('Adding next day')
    df.index = pd.to_datetime(df.index)  # converts from string to datetime
    next_day = df.index[-1] + pd.Timedelta(1, unit='day')
    # advance until not weekend
    while next_day.weekday() > 4:
        next_day += pd.Timedelta(1, unit='day')
    # append to end of dataframe
    logging.info('Appending')
    df.loc[next_day] = None
    df.index = pd.to_datetime(df.index)  # converts from string to datetime
    # actually interpolate
    df = df.interpolate(
        method='spline',
        order=1,
        limit_direction='forward',
        limit_area='outside'
    )
    df.index = df.index.astype(str)  # back to string frm datetime
    logging.info('Extrapolation complete.')
    return df
