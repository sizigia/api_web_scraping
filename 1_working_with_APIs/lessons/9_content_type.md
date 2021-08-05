## Content Type

The server sends more than a status code and the data when it generates a response. It also sends metadata with information on how it generated the data and how to decode it. This information appears in the response headers. We can access it using the `.headers` property.

The headers will appear as a dictionary. For now, the `content-type` within the headers is the most important key. It tells us the format of the response, and how to decode it. For the OpenNotify API, the format is JSON, so we were able to decode it with JSON earlier.