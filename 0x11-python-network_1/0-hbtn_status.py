#!/usr/bin/python3
"""
Script to fetch https resources
"""


import urllib

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')

line = body.splitlines()
formatted_body = '\n'.join(['\t' + line for line in lines])
print(formatted_body)


if __name__ == "__main__":
    pass
