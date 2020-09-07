from aiohttp import web
import pandas as pd
from sec_process import log, interpolate


async def index(request):
    return web.Response(text='This server expects a post of ')


async def forecast(request):
    data = await request.json()
    await log(data)
    new_data = await interpolate(data)
    if new_data is TypeError:
        return web.Response(text='Error: data not given as json')
    else:
        return web.json_response(new_data, dumps=pd.io.json.dumps)