"""
Instructions:

- Make an authenticated request to https://api.github.com/users/VikParuchuri/orgs. This will give us a list of the organizations a GitHub user belongs to.
- Assign the JSON content of the response to orgs (you can get this with response.json()).
"""
import requests
# Create a dictionary of headers containing our Authorization header.
headers = {"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}

# Make a GET request to the GitHub API with our headers.
# This API endpoint will give us details about Vik Paruchuri.
response = requests.get(
    "https://api.github.com/users/VikParuchuri", headers=headers)

# Print the content of the response.  As you can see, this token corresponds to the account of Vik Paruchuri.
print(response.json())

response_orgs = requests.get(
    "https://api.github.com/users/VikParuchuri/orgs", headers=headers)
orgs = response_orgs.json()

print(orgs)
