#!/usr/bin/python3
import sys

n = len(sys.argv)

if (n == 1):
    print("0 arguments.")
else:
    for i in range(1, n):
        print('{}'.format(sys.argv[i], end=" "))

