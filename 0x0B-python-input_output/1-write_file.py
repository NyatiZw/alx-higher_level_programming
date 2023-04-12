#!/usr/bin/python3

"""
Function to write text file

"""


def read_file(filename="", text=""):
    """Function to write text file

    Args:
        filename: files name
        text: file contents

    """

    with open('', encoding="utf-8") as f:
        read_file = f.read()

    print("{}".format(read_file))
