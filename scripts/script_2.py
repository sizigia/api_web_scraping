"""
Instructions:

- Make a GET request to http://api.open-notify.org/iss-pass.
- Assign the status code of the response to status_code.
"""

import pickle
import requests

response = requests.get('http://api.open-notify.org/iss-pass')

status_code = response.status_code

status_meaning = {
    '200': "Everything went okay, and the server returned a result(if any).",
    '301': "The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or when an endpoint's name has changed.",
    '401': "The server thinks you're not authenticated. This happens when you don't send the right credentials to access an API.",
    '400': "The server thinks you made a bad request. This can happen when you don't send the information that the API requires to process your request(among other things).",
    '403': "The resource you're trying to access is forbidden, and you don't have the right permissions to see it.",
    '404': "The server didn't find the resource you tried to access."
}

pickle.dump(status_meaning, open(
    'api_web_scraping/scripts/status_dict.pkl', 'wb'))

print(f"{status_meaning[str(status_code)]} ({status_code})")
