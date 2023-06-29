#!/bin/bash
# Script that takes in a URL, sends Request and displays size of the body Response

response=$(curl -sI 0.0.0.0:5000)
content_length=$(echo "$response" | awk -F': ' '/Content-Length/ { print $2 }')

echo "$content_length"
