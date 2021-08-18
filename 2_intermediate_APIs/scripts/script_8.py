"""
Instructions:

- Make a DELETE request to the https://api.github.com/repos/VikParuchuri/learning-about-apis endpoint.
- Assign the status_code of the response to the variable status.
"""
import requests
headers = {'Authorization': 'token 1f36137fbbe1602f779300dad26e4c1b7fbab631'}

# Example
response = requests.delete(
    "https://api.github.com/repos/VikParuchuri/test", headers=headers)
print(response.status_code)

# Exercise
response_2 = requests.delete(
    "https://api.github.com/repos/VikParuchuri/learning-about-apis", headers=headers)
status = response_2.status_code
