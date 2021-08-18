## PUT/PATCH Requests

Sometimes we want to update an existing object, instead of creating a new one. This is where *PATCH* and *PUT* requests come into play.

We use *PATCH* requests when we want to change a few attributes of an object, but don't want to resend the entire object to the server. For example, maybe we just want to change the name of our repository.

We use *PUT* requests to send the complete object we're revising as a replacement for the server's existing version.

In practice, API developers don't always respect this convention. Sometimes API endpoints that accept *PUT* requests will treat them like *PATCH* requests, and not require us to send the whole object back.

We send a payload of data with *PATCH* requests, the same way we do with *POST* requests:

```python
payload = {"description": "The best repository ever!", "name": "test"}
response = requests.patch("https://api.github.com/repos/VikParuchuri/test", json=payload)
```

The code above will change the description of the `test` repository to `The best repository ever!` (we didn't specify a description when we created it). We provide the name because the GitHub API specification says this is a required field.

A successful *PATCH* request will usually return a `200` status code.