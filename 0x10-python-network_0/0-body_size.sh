#!/usr/bin/env bash
# Script that takes in a URL, sends Request and displays size of the body Response

URL="$1" # Get the URL from command line

# Send the request and store the response in a variable
response=$(curl -sI "$URL")

# Extract Content-Length header
content_length=$(echo "$response" | awk '/Content-Length/ { print $2 }')

# Display the size in bytes
echo "$content_length"
