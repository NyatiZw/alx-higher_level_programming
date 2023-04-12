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

    with open("filename", "w", encoding="utf-8") as f:
        f.write = text

    with open("filename", encoding="utf-8") as f:
        print("{:s}".format(f.read))

