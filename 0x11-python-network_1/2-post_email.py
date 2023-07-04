#!/usr/bin/python3
"""
Script to send a Post request with emailand display body response
"""

import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    data = urllib.parse.urlencode(email).encode('utf-8')
    req = urllib.request.Request(url, data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')

    print("Your email is:")
    print(body)
