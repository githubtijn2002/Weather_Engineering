# dockerfile python hosting on port 8080
import json

import requests

req = requests.get("https://api.github.com/events")

print(req.status_code)
print(req.json())
print(req.headers)
print(req.text)
print(req.content)


