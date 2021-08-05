## Introduction to API Requests

Organizations host their APIs on **web servers**. When you type `www.google.com` in your browser's address bar, your computer is actually asking the `www.google.com` server for a web page; the server returns the page to your browser.

APIs work much the same way, except instead of your web browser asking for a web page, your program asks for data. The API usually returns this data in [`JavaScript Object Notation`](https://www.json.org/json-en.html) (JSON) format. We'll discuss JSON more later on in this lesson.

We make an API request to the web server with the data we want. The server then replies and sends it to us. In Python, we do this using the [`requests library`](https://docs.python-requests.org/en/master/).