We looked at a basic API in the last lesson. That API didn't require authentication, but most do. Imagine that you're using the reddit API to pull a list of your private messages. It would be a huge privacy breach for reddit to give that information to anyone, so requiring authentication makes sense.

APIs also use authentication for **rate limiting**. Developers typically use APIs to build interesting applications or services. To make sure an API is available and responsive for all users, it will prevent you from making too many requests too quickly. We call this *restriction rate limiting*.

In this lesson, we'll explore the GitHub API and use it to pull some interesting data on repositories and users. GitHub is a site for hosting code. If you haven't looked at it, it's a great place to share a portfolio.

GitHub has user accounts ([example](https://github.com/torvalds)), repositories that contain code ([example](https://github.com/torvalds/linux)), and organizations that companies can create ([example](https://github.com/dataquestio)).

Take a look at the documentation for the [GitHub API](https://developer.github.com/v3/), specifically the [authentication](https://developer.github.com/v3/#authentication) section.