#!/bin/bash
# Script to send a DELETE request to a URL and display the body of the body of the response
curl -s -X DELETE 0.0.0.0:5000 | echo 'I am a DELETE request'
