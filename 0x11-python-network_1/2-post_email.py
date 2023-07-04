#!/usr/bin/python3
"""
Script to send a Post request with emailand display body response
"""

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email: email'}).encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    body = response.read().decode('utf-8')

print("Response body:")
print(body)
