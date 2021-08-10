"""
Instructions:

- Get the second page of repositories that Vik Paruchuri starred from the https://api.github.com/users/VikParuchuri/starred endpoint.
    - Assign the JSON of the response to page2_repos.
"""
import requests
headers = {'Authorization': 'token 1f36137fbbe1602f779300dad26e4c1b7fbab631'}

params = {"per_page": 50, "page": 1}

response = requests.get(
    "https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params)
page1_repos = response.json()


response_2 = requests.get("https://api.github.com/users/VikParuchuri/starred",
                          headers=headers,
                          params={"per_page": 50,
                                  "page": 2})
page2_repos = response_2.json()

print(page2_repos)
