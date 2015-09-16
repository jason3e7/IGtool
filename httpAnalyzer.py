import requests

r = requests.get("http://docs.python-requests.org/en/latest/user/quickstart/")
print r.headers
print r.content
