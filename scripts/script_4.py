"""
Instructions:

- Use a dictionary and the parameters argument to get a response for latitude 37.78 and longitude -122.41 (the coordinates of San Francisco).
- Retrieve the content of the response with response.content.
- Assign the content to the variable content.
"""
import requests


def get_resp_params(city):
    response = requests.get(
        "http://api.open-notify.org/iss-pass.json", params=parameters[city])

    return response


# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {'NYC': {"lat": 40.71, "lon": -74},
              'SF': {"lat": 37.78, "lon": -122.41}}

# Make a get request with the parameters.
response = get_resp_params('NYC')

# Print the content of the response (the data the server returned)
print(response.content)

# This gets the same data as the command above
response = requests.get(
    "http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
print(response.content)

# Latitude and longitude of San Francisco
response = get_resp_params('SF')
content = response.content
print(content)
print(content == requests.get(
    f"http://api.open-notify.org/iss-pass.json?lat={parameters['SF']['lat']}&lon={parameters['SF']['lon']}").content)
