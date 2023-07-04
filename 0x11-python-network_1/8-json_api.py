#!/usr/bin/python3
"""
Script to send a POST request to http://0.0.0.0:5000/search
usage: ./8-json_api.py
"""


import requests
from sys import argv


if __name__ == "__main__":
    url ='http://0.0.0.0:5000/search_user'
    letter = argv[1] if len(argv) > 1 else ""

    resp = requests.post(url, data={'q': letter})

    try:
        data = response.json()
        if isinstance(data, dict):
            if 'id' in data and 'name' in data:
                print("[{}] {}".format(data['id'], data['name']))
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
