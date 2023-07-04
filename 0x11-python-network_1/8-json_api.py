#!/usr/bin/python3
"""
Script to send a POST request to http://0.0.0.0:5000/search
usage: ./8-json_api.py
"""


import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]

    data = {'q': letter}

    resp = requests.post(url, data)

    try:
        dic = resp.json()
        if isinstance(dic, dict):
            if 'id' in dic and 'name' in dic:
                print("[{}] {}".format(dic['id'], dic['name']))
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
