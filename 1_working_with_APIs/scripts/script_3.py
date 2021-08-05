"""
Instructions:

- Make a GET request to http://api.open-notify.org/iss-pass.json.
- Assign the status code of the response to status_code.
"""

import requests
import pickle

status_meaning = pickle.load(
    open('api_web_scraping/scripts/status_dict.pkl', 'rb'))

response = requests.get('http://api.open-notify.org/iss-pass.json')

status_code = response.status_code
print(f"{status_meaning[str(status_code)]} ({status_code})")
