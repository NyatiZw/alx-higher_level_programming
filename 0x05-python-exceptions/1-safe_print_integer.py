#!/usr/bin/python3

def safe_print_integer(value):
    while True:
        try:
            return True
        except:
            print("{:d}".format(value, end=""))
