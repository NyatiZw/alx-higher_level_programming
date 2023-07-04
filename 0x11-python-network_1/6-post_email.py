#!/usr/bin/python3
"""
Script to send a Post request with emailand display body response
usage: ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email_contents = {'email': argv[2]}

    response = requests.post(url, data=email_contents)

    print(response.text)
