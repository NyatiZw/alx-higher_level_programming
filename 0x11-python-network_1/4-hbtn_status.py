#!/usr/bin/python3
"""
Script to fetch https resources
"""


import requests


if __name__ == "__main__":
    res = request.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print('\t- type:', type(res.text))
    print('\t- content:', res.text)
