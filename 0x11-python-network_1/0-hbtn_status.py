#!/usr/bin/python3
"""
Script to fetch https resources
"""


import urllib.request

resource = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(resource) as response:
    body = response.read().decode('utf-8')

line = body.splitlines()
formatted_body = '\n'.join(['\t' + line for line in lines])
print(formatted_body)


if __name__ == "__main__":
