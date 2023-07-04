#!/usr/bin/python3
"""
Script that takes in a url, sends request to url and displays x-request
"""

import urllib.request
from sys import argv

url = argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        x_request_id = headers.get('X-Request-Id')
    print(x_request_id)
