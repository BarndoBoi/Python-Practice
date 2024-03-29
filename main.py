import requests
from pprint import pprint
import sys

response = requests.get('https://github.com/BarndoBoi') #Fetch my github profile
pprint(response.text)

if len(sys.argv) > 1:
    output_to_file = sys.argv[1]
else:
    output_to_file = None

if output_to_file == "true":
    #Dump the response text to a file for viewing
    with open("response.html", "w") as file:
        file.write(response.text)
