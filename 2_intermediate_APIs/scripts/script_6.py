"""
Instructions:

- Create a repository named learning-about-apis.
- Assign the status code of the response to the status variable.
"""
import requests

headers = {'Authorization': 'token 1f36137fbbe1602f779300dad26e4c1b7fbab631'}

# Create the data we'll pass into the API endpoint.  While this endpoint only requires the "name" key, there are other optional keys.
payload = {"name": "test"}

# We need to pass in our authentication headers!
response = requests.post(
    "https://api.github.com/user/repos", json=payload, headers=headers)
print(response.status_code)

payload_2 = {'name': 'learning-about-apis'}
response_2 = requests.post(
    "https://api.github.com/user/repos", json=payload_2, headers=headers)

status = response_2.status_code
