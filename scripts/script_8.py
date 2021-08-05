"""
Instructions:

- Find how many people are currently in space.
- Assign the result to in_space_count.
"""
# Call the API here.
import requests

response = requests.get("http://api.open-notify.org/astros.json")

json_data = response.json()

in_space_count = json_data["number"]
print(in_space_count)
