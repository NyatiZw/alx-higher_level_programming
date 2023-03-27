#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for x in my_list[1:]:
        try:
            safe_print_list()
        except Result as res:
            print('{:d}'.format(my_list[x]))
