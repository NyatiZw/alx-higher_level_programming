#!/bin/bash
# script that takes URL, sends a GET request to the URL and display the body of the response
curl -s -L "$1"
