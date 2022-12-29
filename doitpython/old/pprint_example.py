from pprint import pprint
from urllib import request
import json
response = request.urlopen("https://jsonplaceholder.typicode.com/users")
json_response = response.read()
users = json.loads(json_response)

pprint(users)
