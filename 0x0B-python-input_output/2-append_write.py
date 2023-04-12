#!/usr/bin/python3
"""
Function to append text file

"""


def append_file(filename="", text=""):

    """Function to write text file

    Args:
        filename: files name
        text: file contents

    """

    with open("filename", "w", encoding="utf-8") as f:
        text = f.write
        length = len(text)

    with open("filename", encoding="utf-8") as f:
        print("{}".format(length.read))
