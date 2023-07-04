#!/usr/bin/python3
"""
Script to send a Post request with emailand display body response
"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email: email'}).encode('utf-8')
    req = urllib.request.Request(url, datad=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')

    print("Response body:")
    print(body)
