#!/usr/bin/python3

def safe_print_division(a, b):

    result = int(a // b)
    try:
        print("{:d} / {:d}".format(a, b, result,))
    except:
        print("None")
    finally:
        print("Inside result: {:d}".format(result))
