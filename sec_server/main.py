from aiohttp import web
from routes import setup_routes
import logging
# import os

# set up logging function
# NOTE: this is currently synchronous, which is a problem
logging.basicConfig(
    format='%(asctime)s %(message)s',
    filename='sec_server_log.txt',
    level=logging.INFO
)


# run server
app = web.Application()
setup_routes(app)
web.run_app(app, port=8080)
