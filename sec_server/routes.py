from aiohttp import web

from views import forecast, index, window_forecast


def setup_routes(app: web.Application) -> None:
    """
    Sets up routes for various requests.

    index: static html testing page

    window_forecast: given json containing "ticker" and "window" uses yfinance
    to send back an extrapolation based on the last window days of that stock
    ticker.
    TODO: add mongodb / motor integration

    forecast:  takes in a json serialized dataframe of prices that has
    securities as columns and is datetime indexed, and then returns a json
    serialized dataframe with the next day added as a linear interpolation

    """
    app.router.add_get('/', index)
    app.router.add_post('/window_forecast', window_forecast)
    app.router.add_post('/forecast', forecast)
