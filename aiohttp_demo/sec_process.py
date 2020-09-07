import os
import pandas as pd
import json

current_directory = str(os.getcwd())


def extrapolate(earlier, later):
    """Basic function to perform linear extrapolation of two numbers"""
    return (later - earlier) + later


async def log(data, error=False):
    """Logs incoming data in data file"""
    log_file = open((current_directory + '_log.txt'), 'a')
    if error is True:  # Currently unused
        log_file.write("ERRONEOUS DATA:", '\n')
    log_file.write(str(data))
    log_file.write('\n')
    log_file.close()


async def process(data):
    """Converting incoming data to dataframe"""
    df = pd.DataFrame(data)
    return df


async def interpolate(data):
    """Takes the dataframe made by process and adds a new row with
    extrapolated data and returns it."""
    df = await process(data)
    if df is TypeError:
        return TypeError
    next_day = df.index[-1] + pd.Timedelta(1, unit='day')
    df.loc[next_day] = [i for i in map(extrapolate, df.iloc[-2], df.iloc[-1])]
    jdf = pd.to_json(df)
    return jdf
