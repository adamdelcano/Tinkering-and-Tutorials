import logging

from aiohttp import web
import motor.motor_asyncio

from routes import setup_routes

# set up logging function
# NOTE: this is currently synchronous
logging.basicConfig(
    format='%(asctime)s %(message)s',
    filename='sec_server_log.txt',
    level=logging.INFO
)

# initiate connection with mongodb and get collection, because motor rules
# this is technically a specific collection, might be worth renaming?
db = motor.motor_asyncio.AsyncIOMotorClient(
    'mongodb://baxter:stockman@localhost:27017/admin'
).stock.history


# run server
if __name__ == '__main__':
    app = web.Application()
    app['db'] = db
    setup_routes(app)
    web.run_app(app, port=8080)
