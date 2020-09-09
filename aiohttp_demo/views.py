from aiohttp import web
import pandas as pd
from sec_process import log, extrapolate
import json


async def index(request):
    return web.Response(text='This server expects a post of json data.')


async def forecast(request):
    """Takes json post, logs it, processes it, returns it."""
    try:
        data = await request.json()
        await log(data, 'json received:')
    # initial error handling, is insufficiently robust
    except json.decoder.JSONDecodeError:
        await log(request, 'Data received as non-json format:')
        return web.Response(text="""
            Error: server was unable to parse request's json.
            """)
    new_data = await extrapolate(data)
    return web.json_response(new_data, dumps=pd.io.json.dumps)
