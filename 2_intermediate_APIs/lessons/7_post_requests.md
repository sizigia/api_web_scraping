## POST Requests

So far, we've been making *GET* requests. We use *GET* requests to retrieve information from a server (hence the name GET). There are a few other types of API requests.

For example, we use *POST* requests to send information (instead of retrieve it), and to create objects on the API's server. With the GitHub API, we can use *POST* requests to create new repositories.

Different API endpoints choose what types of requests they will accept. Not all endpoints will accept a *POST* request, and not all will accept a *GET* request. You'll have to consult the [API's documentation](https://developer.github.com/v3/) to figure out which endpoints accept which types of requests.

We can make *POST* requests using `requests.post`. *POST* requests almost always include data, because we need to send the data the server will use to create the new object.

We pass in the data in a manner similar to what we do with query parameters and *GET* requests:

```python
payload = {"name": "test"}
requests.post("https://api.github.com/user/repos", json=payload)
```

The code above will create a new repository named `test` under the account of the currently authenticated user. It will convert the payload dictionary to JSON and pass it along with the *POST* request.

Check out GitHub's [API documentation for repositories](https://developer.github.com/v3/repos/) to see a full list of what data we can pass in with this *POST* request. Here are just a couple data points:

- `name` — required, the name of the repository
- `description` — optional, the description of the repository

A successful *POST* request will usually return a `201` [status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) indicating that it created the object on the server. Sometimes, the API will return the JSON representation of the new object as the content of the response.

