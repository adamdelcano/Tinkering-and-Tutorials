from aiohttp import web
import pandas as pd
from sec_process import extrapolate
import json
import logging


async def index(request: web.Request) -> web.Response:
    """ Returns a static landing page to non-post requests. """
    logging.info(f'Received {request} non-post request')
    static_page = """<!DOCTYPE html>
<html>
  <title>If You're Here, Something Has Gone Wrong</title>

  <h1>Something has gone terribly wrong</h1>
  <p>Okay, not <i>that</i> wrong.</p>
  <p>This is just my shoddy static landing page.
  Right now you want to add '/forecast' to the URL you used to navigate here
  and then send a POST request containing a json serialized dataframe.</p>
  <p>Or not, it's not that interesting.</p>
  <p> </p>
  <p>Also if you're here because I (Adam) asked you to help me test this,
   I guess it's actually the <b>opposite</b> of something going wrong?</p>
</html>"""
    return web.Response(text=static_page, content_type='text/html')


async def forecast(request: web.Request) -> web.json_response:
    """Takes json post, logs it, processes it, returns it."""
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
