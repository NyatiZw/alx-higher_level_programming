#!/bin/bash
# script that takes URL, sends a request, and displays the size of the body of the response
curl -sI 0.0.0.0:5000 | awk -F': ' '/Content-Length/{ print $2 }'
