#!/usr/bin/python3

# Function that prints a dictionary by ordered keys
def print_sorted_dictionary(a_dictionary):
    ordered_list = list(a_dictionary.keys())
    ordered_list.sort()
    for j in ordered_list:
        print("{}: {}".format(j, a_dictionary.get(j)))
