## User-Level Endpoints

So far, we've looked at endpoints where we need to explicitly provide the username of the person whose information we're looking up. For example, we used `https://api.github.com/users/VikParuchuri/starred` to pull up the repositories that `VikParuchuri` starred.

Since we've authenticated with our token, the system knows who we are, and it can show us some relevant information without us specifying our username.

Making a *GET* request to `https://api.github.com/user` will give us information about the user the authentication token is for.

There are other endpoints that behave like this. They automatically provide information or allow us to take actions as the authenticated user.