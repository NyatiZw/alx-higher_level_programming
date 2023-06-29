#!/bin/bash
content_length=$(curl -sI 0.0.0.0:5000 | awk -F': ' '/Content-Length/ { print $2 }')
echo "$content_length"
