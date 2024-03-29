import requests
from pprint import pprint
import sys, os
import json

github_url = 'https://api.github.com'
username = 'BarndoBoi'

"""Header information here. Not using Github API's version info as we want the latest."""
accept_header = 'application/vnd.github+json'
user_agent = 'VickyHub/0.0.1'
headers = {'user-agent' : user_agent, 'accept' : accept_header}

#Dictionary stores the name of the endpoint, then a tuple with the request type and the endpoint's url
endpoints = {'User': '/users/' + username}

response = requests.get(github_url + endpoints['User'], headers=headers)
pprint(response.text)

folder_path = 'data_dumps'
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, 'json_response.json')

if response.json():
    with open(file_path, 'w') as file:
        file.write(json.dumps(response.json(), indent=4))

if len(sys.argv) > 1:
    output_to_file = sys.argv[1]
else:
    output_to_file = None

if output_to_file == 'true':
    #Dump the response text to a file for viewing
    with open('response.html', 'w') as file:
        file.write(response.text)