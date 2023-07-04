#!/usr/bin/python3
"""
Script to display Github user ID using the Github API
"""


import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    usrname = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(usrname, token)

    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data["id"]
        print("user_id")
    else:
        print("None")
