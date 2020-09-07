from views import index, forecast


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_post('/', forecast)
