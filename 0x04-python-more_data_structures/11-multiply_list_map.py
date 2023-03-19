#!/usr/bin/python3
# Function that returns all values multiplied by n without using loops
def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda x: x * number), my_list)))
