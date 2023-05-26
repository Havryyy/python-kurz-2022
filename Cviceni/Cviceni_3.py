import requests

response = requests.get('https://api.kodim.cz/python-data/people')
data = response.json()
for jmeno in response:
    