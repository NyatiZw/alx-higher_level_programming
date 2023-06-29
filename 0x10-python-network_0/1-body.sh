#!/bin/bash
# script that takes URL, sends a GET request to the URL and display the body of the response
curl -s -w "200" "$1" | awk '/^$/ {p=0} p; /Body/ {p=1}'
