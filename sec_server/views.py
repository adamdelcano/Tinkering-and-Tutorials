import json
import logging

from aiohttp import web

import pandas as pd

from sec_process import extrapolate


async def index(request: web.Request) -> web.Response:
    """ Returns a static landing page to non-post requests.

    At this time, this is just an extremely basic function, which takes in any
    web.Request object sent to it, logs it, and serves it, regardless of what
    it is, the same static html.

    Receives a non-POST request as sole parameter, returns web.Response."""
    logging.info(f'Received {request} non-post request')
    static_page = open('./test_page.html', 'r').read()

    return web.Response(text=static_page, content_type='text/html')


async def forecast(request: web.Request) -> web.json_response:
    """
    Takes json post, logs it, processes it, returns it.

    forecast takes the web.Request, logs it, attempts to decode
    the json data in it, runs that through extrapolate (in sec_process.py)
    and after logging that, returns a web.json_response using pd.io.json.dumps
    as the dumps format. Note that logging is blocking.

    Takes web.Request object as sole parameter (should be POST w/ json) and
    returns a processed web.json_response object.
    """
    logging.info(f'Received {str(request)}')
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
    logging.info(f'Sending {str(new_data)}')
    return web.json_response(new_data, dumps=pd.io.json.dumps)
