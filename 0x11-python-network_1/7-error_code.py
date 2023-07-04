#!/usr/bin/python3
"""
Script to send a request to a URL and display the response body
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:" response.status_code)
    else:
        print(response.text)
