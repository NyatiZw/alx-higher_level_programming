#!/usr/bin/python3
"""
Function to write text file

"""


def write_file(filename="", text=""):

    """Function to write text file

    Args:
        filename: files name
        text: file contents

    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
