"""
Instructions:

- Get the duration value of the ISS's first pass over San Francisco and assign the value to first_pass_duration.
"""
import requests
# Make the same request we did two screens ago.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get(
    "http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a Python object.  Verify that it's a dictionary.
json_data = response.json()
print(type(json_data))
print(json_data)

first_pass_duration = json_data["response"][0]["duration"]
print(first_pass_duration)
