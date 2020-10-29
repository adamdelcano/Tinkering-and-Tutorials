import logging

import pandas as pd


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
