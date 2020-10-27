import pandas as pd
import logging


async def process(data: dict) -> pd.DataFrame:
    """Converting incoming data to dataframe. Currently in need of expansion
    to handle basic data sanitization and error checking, would not be in
    it's own function otherwise."""
    logging.info(f'Converting {data} to dataframe')
    df = pd.DataFrame(data)
    return df


async def extrapolate(data: dict) -> str:
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
    df.index = df.index.astype(str)  # back to string from datetime
    logging.info('Extrapolation complete.')
    return df
