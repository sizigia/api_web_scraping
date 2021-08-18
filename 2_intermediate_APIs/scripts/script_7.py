"""
Instructions:

- Make a PATCH request to the https://api.github.com/repos/VikParuchuri/learning-about-apis endpoint that changes the description to Learning about requests!.
- Assign the status code of the response to status.
"""
import requests
headers = {'Authorization': 'token 1f36137fbbe1602f779300dad26e4c1b7fbab631'}

# Example
payload = {"description": "The best repository ever!", "name": "test"}
response = requests.patch(
    "https://api.github.com/repos/VikParuchuri/test", json=payload, headers=headers)
print(response.status_code)

# Exercise
payload_2 = {"description": "Learning about requests!",
             "name": "learning-about-apis"}
response_2 = requests.patch(
    "https://api.github.com/repos/VikParuchuri/learning-about-apis", json=payload_2, headers=headers)

status = response_2.status_code
print(status)
