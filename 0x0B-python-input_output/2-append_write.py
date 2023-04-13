#!/usr/bin/python3
"""
Function to append text file

"""


def append_write(filename="", text=""):

    """Function to append text file

    Args:
        filename: files name
        text: file contents

    """

    with open("filename", "a", encoding="utf-8") as f:
        return f.append(text) 
