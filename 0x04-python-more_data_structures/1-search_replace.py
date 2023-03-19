#!/usr/bin/python3

# Function to replace element in a list
def search_replace(my_list, search, replace):
    res = list(map(lambda a: replace if a == search else a, my_list))
    return (res)
