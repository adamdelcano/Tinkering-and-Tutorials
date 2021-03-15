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

#### Test Curl Example
curl 0.0.0.0:8080 -X POST --header "Content-Type: application/json" -d '{"US Equity 1": {"2019-12-31 00:00:00": 292.09690559, "2020-01-01 00:00:00": null, "2020-01-02 00:00:00": 297.7793125908, "2020-01-03 00:00:00": 298.9785784171, "2020-01-06 00:00:00": 296.6245466, "2020-01-07 00:00:00": 298.7233884743, "2020-01-08 00:00:00": 298.3613397805, "2020-01-09 00:00:00": 308.1441646202, "2020-01-10 00:00:00": 311.6581942031}, "US Equity 2": {"2019-12-31 00:00:00": 44.8708282107, "2020-01-01 00:00:00": null, "2020-01-02 00:00:00": 45.5908218567, "2020-01-03 00:00:00": 45.2092292074, "2020-01-06 00:00:00": 44.701675083, "2020-01-07 00:00:00": 44.7303561789, "2020-01-08 00:00:00": 44.8757338433, "2020-01-09 00:00:00": 45.4057031743, "2020-01-10 00:00:00": 45.6358447162}, "US Equity 3": {"2019-12-31 00:00:00": 69.2100089516, "2020-01-01 00:00:00": null, "2020-01-02 00:00:00": 69.981577095, "2020-01-03 00:00:00": 69.4779153965, "2020-01-06 00:00:00": 69.2674830232, "2020-01-07 00:00:00": 69.3902453497, "2020-01-08 00:00:00": 69.4126846558, "2020-01-09 00:00:00": 69.6637721187, "2020-01-10 00:00:00": 69.6777659411}, "US Equity 4": {"2019-12-31 00:00:00": 212.281148486, "2020-01-01 00:00:00": null, "2020-01-02 00:00:00": 214.9633213722, "2020-01-03 00:00:00": 214.4980057465, "2020-01-06 00:00:00": 213.7532451512, "2020-01-07 00:00:00": 215.3900870373, "2020-01-08 00:00:00": 216.2407376124, "2020-01-09 00:00:00": 218.923596033, "2020-01-10 00:00:00": 219.532067974}}'

Updated Functionality: 
TODO: 
Handle requests in the form of
{
  Ticker: <string>
  Window: <number of days>
}
You are going to check if you have the last Window days of the price of Ticker in your database
If you do not then use https://github.com/ranaroussi/yfinance to fetch the price and save it into the database.  If you do then just use that.  If you have a partial selection of data then you should only request the subset of data you do not have.
Once you have the last Window days you are going to do anything you want (linear interpolation is fine) to give me the projected price tomorrow for the ticker
ranaroussi/yfinance
Yahoo! Finance market data downloader (+faster Pandas Datareader)
Website
https://aroussi.com/post/python-yahoo-finance
Stars
3410
<https://github.com/ranaroussi/yfinance|ranaroussi/yfinance>ranaroussi/yfinance | May 21st, 2017 | Added by GitHub
