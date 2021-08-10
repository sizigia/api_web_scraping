## API Authentication

To authenticate with the GitHub API, we need to use an access token. An access token is a credential we can [generate on GitHub's website](https://github.com/settings/tokens). The token is a string that the API can read and associate with your account.

Using a token is better than using a username and password for a few reasons:

- Typically, you'll be accessing an API from a script. If you put your username and password in the script and someone finds it, they can take over your account. However, you can revoke an access token to cancel an unauthorized person's access if there's a security breach.
- Access tokens can have scopes and specific permissions. For example, you can make a token that has permission to write to your GitHub repositories and make new ones. You can also make a token that can only read from your repositories. Using read-access-only tokens in potentially insecure or shared scripts improves security.

You need to pass your token to the GitHub API through an *authorization header*. Just like the server sends headers in response to our request, we can send the server headers when we make a request. Headers contain metadata about the request. We can use Python's `requests` library to make a dictionary of headers, and then pass it into our request.

We need to include the word `token` in the authorization header, followed by our access token. Here's an example of an authorization header:

```python
{"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}
```

In this case, our access token is `1f36137fbbe1602f779300dad26e4c1b7fbab631`. GitHub generated this token and associated it with the account belonging to `Vik Paruchuri`.

You should **never** share your token with anyone you don't want to have access to your account. We've revoked the token you'll be using throughout this lesson, so it isn't valid anymore. Consider a token somewhat equivalent to a password, and store it securely.

We've imported `requests` for you already, so you don't need to do it again in this lesson. Importing `requests` will overwrite some of the custom API logic we've developed for answer checking.