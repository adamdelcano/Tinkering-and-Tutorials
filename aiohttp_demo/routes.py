from views import index, forecast


def setup_routes(app):
    """ Just has route for forecast and a basic index route."""
    app.router.add_get('/', index)
    app.router.add_post('/', forecast)
