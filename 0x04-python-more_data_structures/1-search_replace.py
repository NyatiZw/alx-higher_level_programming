#!/usr/bin/python3

def search_replace(my_list, search, replace):
# Function to replace element in a list
    res = list(map(lambda a: replace if a == search else a, my_list))
    return (res)
