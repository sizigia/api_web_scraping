"""
Introductions:

- Make a GET request to the https://api.github.com/repos/octocat/Hello-World endpoint.
    - Assign the JSON result to hello_world.
"""
import requests

headers = {'Authorization': 'token 1f36137fbbe1602f779300dad26e4c1b7fbab631'}

response = requests.get(
    "https://api.github.com/repos/octocat/Hello-World", headers=headers)

hello_world = response.json()

print(hello_world)
