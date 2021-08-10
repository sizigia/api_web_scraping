## Pagination

Sometimes, a request can return many objects. This might happen when you're listing out all of a user's repositories, for example. Returning too much data will take a long time and slow the server down. For example, if a user has 1,000+ repositories, requesting all of them might take 10+ seconds. This isn't a great user experience, so it's typical for API providers to implement **pagination**. This means that the API provider will only return a certain number of records per page. You can specify the page number that you want to access. To access all of the pages, you need to write a loop.

To get the repositories a user has starred (marked as interesting), we can use the following API endpoint:

`https://api.github.com/users/VikParuchuri/starred`

We can add two pagination query parameters to it: `page`, and `per_page`. `page` is the page we want to access, and `per_page` is the number of records we want to see on each page. Typically, API providers enforce a cap on how high `per_page` can go, because setting it to an extremely high value defeats the purpose of pagination.

Check out the [Github API documentation on pagination](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#pagination).
