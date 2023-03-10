#!/usr/bin/python3
import sys

if __name__ == "__main__":

    n = len(sys.argv)

    if (n == 1):
        print("0 arguments.")

    for i in range(1, n):
        if (n >= 2):
            print('{} arguments'.format(i, end=" "))
        elif (n == 1):
            print('{} argument'.format(i, end=" "))
