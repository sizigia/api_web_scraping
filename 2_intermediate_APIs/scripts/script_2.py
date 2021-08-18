"""
Instructions:

- Use the endpoint https://api.github.com/users/torvalds with the same headers from before to get information about Linus Torvalds.
    - Use the response.json() method to get the JSON of the response.
    - Assign the result to torvalds.
"""
import requests
# Create a dictionary of headers containing our Authorization header.
headers = {"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}

# Make a GET request to the GitHub API with our headers.
response = requests.get(
    "https://api.github.com/users/torvalds", headers=headers)

torvalds = response.json()

# Print the content of the response.
print(torvalds)
