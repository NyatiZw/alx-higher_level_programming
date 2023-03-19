#!/usr/bin/python3

# Function that adds all integers in a list
def uniq_add(my_list=[]):
    res = set(my_list)
    n = 0

    for j in res:
        n += j

    return (n)
