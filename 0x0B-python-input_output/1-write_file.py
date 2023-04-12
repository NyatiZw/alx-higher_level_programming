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

    with open("filename", "rw", encoding="utf-8") as f:
        f.write = text
        print(f.read)

