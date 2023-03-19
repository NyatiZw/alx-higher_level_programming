#!/usr/bin/python3

# Function that returnns the number keys in a dictionary
def number_keys(a_dictionary):
    number = 0
    keys = list(a_dictionary.keys())

    for k in keys:
        number += 1

    return (number)
