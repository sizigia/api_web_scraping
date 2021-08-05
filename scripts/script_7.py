"""
Instructions:

- Get content-type from response.headers.
- Assign the content type to the content_type variable.
"""
import requests

response = requests.get("http://api.open-notify.org/iss-pass.json",)
# Headers is a dictionary
print(response.headers)

content_type = response.headers['content-type']
print(content_type)
