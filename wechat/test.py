import requests
import json

url = 'http://192.168.0.10:5000/chatbot/'
payload = {'text': 'Where am I?'}
headers = {'Content-Type': 'application/json'}

# GET
#r = requests.get(url)

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=payload)

# POST with JSON
r = requests.post(url, data=json.dumps(payload), headers=headers)

# Response, status etc
print r
print r.status_code
print r.content
