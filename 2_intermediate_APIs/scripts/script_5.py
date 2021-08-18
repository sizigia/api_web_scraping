"""
Instructions:

- Make a GET request to the "https://api.github.com/user" endpoint.
    - Assign the JSON of the result to the user variable.
"""
import requests
headers = {'Authorization': 'token 1f36137fbbe1602f779300dad26e4c1b7fbab631'}

response = requests.get('https://api.github.com/user', headers=headers)

user = response.json()
print(user)
