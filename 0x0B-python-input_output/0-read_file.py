#!/usr/bin/python3

"""
Function to read text file

"""


def read_file(filename=""):
    """Function to read text file

    Args:
        filename: files name

    """

    while filename != None:
        with open('', encoding="utf-8") as f:
            read_file = f.read()

    print("{}".format(read_file))
