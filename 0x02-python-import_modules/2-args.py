#!/usr/bin/python3
import sys

n = len(sys.argv)

for i in range(1, n):
    print('{}'.format(sys.argv[i], end=" "))
