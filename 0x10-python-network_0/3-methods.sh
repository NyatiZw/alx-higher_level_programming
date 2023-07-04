#!/bin/bash
# Script that takes URL and displays all HTTO methods

curl -s -I "$1" | awk -F': ' '/^Allow/ { print $2 }'
