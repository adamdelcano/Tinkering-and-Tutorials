
# TODO Create an HTTP server that runs on localhost and serves a single endpoint /forecast. This forecast endpoint will take in a json serialized dataframe of prices that has securities as columns and is datetime indexed.

# TODO You must produce a json serialized dataframe that is a linear interpolation of what the next trading day will produce.  So for a given security if you have 9/3 that is $1 and 9/4 that is $2 and 9/4 that is $3 you might predict 9/5 is $4 for this security.

# TODO There may be null values, the security may not have traded that day for some reason (perhaps it is all gibbons day in west pennslytucky where this is traded, I don't know - do you?). You must skip these and still provide an interpolated result. If you have one or zero data points for a security you must return Nan/None or some other non-numerical value.


# TODO figure out what the above means means

# TODO learn wtf aiohttp is so I can make an http server

# TODO produce pandas stuff to take in the values

# TODO figure out linear interpolation algorithm

# TODO add in mechanism for handling null values etc

# TODO documentation check

# TODO make sure it's being logged

# TODO review error handling