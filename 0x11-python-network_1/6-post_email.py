#!/usr/bin/python3
"""
Script to send a Post request with emailand display body response
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    data = {"email": email}
    response = requests.post(url, data=data)

    print(response.text)
