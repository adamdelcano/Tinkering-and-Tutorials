import logging

from aiohttp import web

from routes import setup_routes

# set up logging function
# NOTE: this is currently synchronous
logging.basicConfig(
    format='%(asctime)s %(message)s',
    filename='sec_server_log.txt',
    level=logging.INFO
)


# run server
if __name__ == '__main__':
    app = web.Application()
    setup_routes(app)
    web.run_app(app, port=8080)
