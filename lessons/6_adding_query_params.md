## Adding Query Parameters

In the last example, we got a `400` status code, which indicates a bad request. If we look at the documentation for the OpenNotify API, we see that the [`ISS Pass`](http://open-notify.org/Open-Notify-API/ISS-Pass-Times/) endpoint requires two *parameters*.

The ISS Pass endpoint tells us when the ISS will pass over a given location on the Earth.

To request this information, we need to pass the coordinates for a specific location to the API. We do this by passing two parameters: latitude and longitude.

To do this, we can add an optional keyword argument, `params`, to our request. In this case, we need to pass in two parameters:

- `lat` — the latitude of the location
- `lon` — the longitude of the location
We can make a dictionary that contains these parameters, and then pass them into the function.

We can also do the same thing directly by adding the query parameters to the url, like this:

http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74

It's almost always better to set up the parameters as a dictionary, because the `requests` library we mentioned earlier takes care of certain issues, like properly formatting the query parameters.