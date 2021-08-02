"""
We've imported requests for you already, so you don't need to do it again in this lesson. Importing requests will overwrite some of the custom API logic we've developed for answer-checking in this lesson.

Instructions:
- The server will send a status code indicating the success or failure of your request. You can get the status code of the response from response.status_code.
- Assign the status code to the variable status_code.
"""
import requests

# Make a get request to get the latest position of the ISS from the OpenNotify API.
response = requests.get("http://api.open-notify.org/iss-now.json")

status_code = response.status_code
print(status_code)
