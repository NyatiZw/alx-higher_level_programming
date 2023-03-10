#!/usr/bin/python3
import sys

n = len(sys.argv)

if (n == 1):
    print("0 arguments.")
elif (n > 1):
    for i in range(1, n):
        print('{}'.format(i, end=" "))

