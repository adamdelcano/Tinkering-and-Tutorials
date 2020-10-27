from views import index, forecast
from aiohttp import web


def setup_routes(app: web.Application) -> None:
    """ Just has route for forecast and a basic index route."""
    # TODO: Probably either set up a route table or make flask-style decorators
    app.router.add_get('/', index)
    app.router.add_post('/', forecast)
