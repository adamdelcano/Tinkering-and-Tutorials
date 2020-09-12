from aiohttp import web
import pandas as pd
from sec_process import extrapolate
import json
import logging


async def index(request):
    logging.info('Received %s non-post request at %(asctime)s.', request)
    return web.Response(text='This server expects a post of json data.')


async def forecast(request):
    """Takes json post, logs it, processes it, returns it."""
    logging.info('Received %s', str(request))
    try:
        data = await request.json()
        logging.info('Json received and decoded.')
    # initial error handling, is insufficiently robust
    except json.decoder.JSONDecodeError:
        logging.warning('Non-json data received! Returned error to sender.')
        return web.Response(text="""
            Error: server was unable to parse request's json.
            """)
    new_data = await extrapolate(data)
    logging.info('Sending %s', str(new_data))
    return web.json_response(new_data, dumps=pd.io.json.dumps)
