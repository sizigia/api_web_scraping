You may have noticed that the API response we received earlier was a `string`. Strings are how we pass information back and forth through APIs, but it's not easy to get the information we want out of them. How do we know how to decode the string we receive and work with it in Python?

Luckily, there's a format called JSON. (We mentioned it earlier in this lesson.) This format encodes data structures like lists and dictionaries as strings to ensure that machines can read them easily. JSON is the main format for sending and receiving data through APIs.

Python offers great support for JSON through its `json` library. We can convert *lists* and *dictionaries* to JSON, and vice versa. Our ISS Pass data, for example, is a dictionary encoded as a string in JSON format.

The JSON library has two main methods:

- `dumps` — takes in a Python object and converts it to a string
- `loads` — takes in a JSON string and converts it to a Python object
