## DELETE Requests

The final major request type is the *DELETE* request. The *DELETE* request removes objects from the server. We can use the *DELETE* request to remove repositories.

```python
response = requests.delete("https://api.github.com/repos/VikParuchuri/test")
```

The above code will delete the `test` repository from GitHub.

A successful *DELETE* request will usually return a `204` status code indicating that it successfully deleted the object.

Use *DELETE* requests carefully — it's very easy to remove something important by accident.


## Further Exploration

That's it for the major points of working with APIs, but feel free to continue exploring with [your own API token](https://github.com/settings/tokens). Then, consult the [API documentation](https://developer.github.com/v3/) to find good endpoints to query.