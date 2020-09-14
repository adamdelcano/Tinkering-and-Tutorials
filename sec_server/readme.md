A basic server that serves an endpoint /forecast, takes in a json serialized dataframe of prices that has securities as columns and is datetime indexed, and then returns a json serialized dataframe with the next day added as a linear interpolation.

Structure is pretty basic: 
main.py sets up logging and the server itself
routes.py deals with the current routes. Extremely small at the moment as there are only two.
views.py deals with the actual request handling.
Individual files will handle individual processes as the server expands. Currently there's only one:
sec_process.py which handles json interpolation. 



In terms of dependencies: Currently it uses aiohttp, pandas, scipy, and json. The last is used for very minor functionality and may be able to be removed once I have a better error-handling framework.

#### Performance
Right now a major issue is that logging is blocking, which puts a damper on the gains from asyncio. Probably the best option is moving to the aiologging package.
