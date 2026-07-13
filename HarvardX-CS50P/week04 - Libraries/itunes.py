import json # came with python, it is not necesarry to install
import requests
import sys

# INSTALL PACKAGES
# https://pypi.org/project/requests/
# pip install requests

# APIs = Application Programming Interface

# JSON = JavaScript Object Notation
# Librery: https://docs.python.org/3/library/json.html

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()

for result in o['results']:
    print(result["trackName"])


1 hora: 8 minutos