#!/bin/bash
# Script that takes URL and displays all HTTO methods

curl -s OPTIONS -I "$1" | awk -F': ' '/^Allow/ { print $2 }'
