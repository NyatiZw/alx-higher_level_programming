#!/bin/bash
# Script that takes URL and displays all HTTO methods

curl -s -I "$1" | grep 'ALlow:' | cut -f2- -d' '
