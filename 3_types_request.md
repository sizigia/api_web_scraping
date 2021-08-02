There are many different types of requests. The most common is a GET request, which we use to retrieve data.

We can use a simple GET request to retrieve information from the [`OpenNotify`](http://open-notify.org/) API.

OpenNotify has several API endpoints. An **endpoint** is a server route for retrieving specific data from an API. For example, the `/comments` endpoint on the reddit API might retrieve information about comments, while the `/users` endpoint might retrieve data about users.

The first endpoint we'll look at on OpenNotify is the `iss-now.json` endpoint. This endpoint gets the current latitude and longitude position of the ISS. A dataset wouldn't be a good tool for this task because the information changes often, and it involves some calculation on the server.

[Check out the complete list](http://open-notify.org/Open-Notify-API/) of OpenNotify endpoints.