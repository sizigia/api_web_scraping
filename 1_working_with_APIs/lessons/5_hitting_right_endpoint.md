## Hitting the Right Endpoint

`iss-pass` wasn't a valid endpoint, so the API's server sent us a `404` status code in response. We forgot to add `.json` at the end, like the [API documentation](http://open-notify.org/Open-Notify-API/) tells us to do.
