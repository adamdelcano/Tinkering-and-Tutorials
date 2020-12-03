from aiohttp import web

from views import index, ticker_forecast


def setup_routes(app: web.Application) -> None:
    """ Sets up routes for various requests."""
    # TODO: Probably either set up a route table or make flask-style decorators
    # TODO: Once that's done, document using docstring
    app.router.add_get('/', index)
    app.router.add_post('/', ticker_forecast)
    # app.router.add_post('/', forecast)
