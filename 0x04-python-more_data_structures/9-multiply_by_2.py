#!/usr/bin/python3

# Function that returns a new dictionary with all values multiplied by two
def multiply_by_2(a_dictionary):
    res = a_dictionary.copy()
    keys = list(res.keys())

    for k in keys:
        res[k] *= 2

    return (res)
