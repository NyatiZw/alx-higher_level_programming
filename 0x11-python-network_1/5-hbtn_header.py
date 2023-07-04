#!/usr/bin/python3
"""
Script to fetch X-Request-Id value from a URL response header
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[1]

    data = {"email": email}
    response = requests.post(url, data=data)

    print("Response body:")
    print(response.text)
