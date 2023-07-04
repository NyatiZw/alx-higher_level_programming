#!/usr/bin/python3
"""
Script to fetch https resources
"""


import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()
    content_type = type(body)
    content = repr(body)
    utf8_content = body.decode('utf-8')

print("Body response:")
print(f"\t- type: {content_type}")
print(f"\t- content: {content}")
print(f"\t- utf8 content: {utf8_content}")


if __name__ == "__main__":
    pass
