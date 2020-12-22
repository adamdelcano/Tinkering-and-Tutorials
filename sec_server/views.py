import json
import logging

from aiohttp import web
import motor.motor_asyncio
import pandas as pd

from sec_process import extrapolate
from sec_process import Stock


async def index(request: web.Request) -> web.Response:
    """ Returns a static landing page to non-post requests.

    At this time, this is just an extremely basic function, which takes in any
    web.Request object sent to it, logs it, and serves it, regardless of what
    it is, the same static html.

    Receives a non-POST request as sole parameter, returns web.Response."""
    logging.info(f'Received {request} non-post request')
    static_page = open('./test_page.html', 'r').read()

    return web.Response(text=static_page, content_type='text/html')


async def window_forecast(request: web.Request) -> web.json_response:

    """
    Receives a request containing a string/int of ticker and window, and
    uses the Stock class to generate a response, while logging at each step.
    """
    logging.info(f'Received {str(request)}.')
    db = request.app['db']
    try:
        requested_stock = await request.json()
        logging.info('Json received and decoded')
    except json.decoder.JSONDecodeError:
        logging.warning(f'Unparseable data {str(request)}: sent back 400.')
        raise web.HTTPBadRequest(reason='''
            Message was not POST with recognizeable json.
            ''')
    logging.info(f'Processed: {requested_stock}')
    # seems worth it to make it case insensitive
    requested_stock = {
        k.lower(): v for k, v in requested_stock.items()
    }
    current_stock = Stock(
        requested_stock['ticker'],
        requested_stock['window'],
        db
    )
    logging.info(f'Stock: {current_stock}')
    current_stock.get_prices()
    logging.info(f'Prices: {current_stock.prices}')
    await current_stock.extrapolate_next_day()
    logging.info(f'Sending {str(current_stock.next_price)}')
    # feature creep: displaying the history of stock over window days
    if 'history' in requested_stock and (
        requested_stock['history'] in ('y', 'yes', 1, True)
    ):
        return web.Response(
            text=f'''{current_stock.prices}\n
            Prediction:\n
            {pd.io.json.dumps(current_stock.next_price, indent=1)}'''
        )
    else:
        return web.json_response(
            current_stock.next_price,
            dumps=pd.io.json.dumps
        )


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
        raise web.HTTPBadRequest(reason='''
            Message was not POST with recognizeable json.
            ''')
    new_data = await extrapolate(data)
    logging.info(f'Sending {str(new_data)}')
    return web.json_response(new_data, dumps=pd.io.json.dumps)
