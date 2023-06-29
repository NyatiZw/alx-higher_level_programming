#!/bin/bash
# Script that takes URL and displays all HTTO methods

curl -s -X OPTIONS -I 0.0.0.0:5000 | awk -F': ' '/^Allow/ { print $2 }'
