#!/usr/bin/python3
"""

Function that prints a text with two new lines 

"""


def text_indentation(text):
    """ Function that prints a text with two new lines

    Args:
        text: string member

    Raises:
        TypeError: if member is not a string

    Returns:
        Nothing


    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = text[:]

    for x in ". ? :":
        text_split = string.split(x)
        string = ""
        for j in text_split:
            j = j.strip(" ")
            string = j + x if string is "" else string + "\n\n" + j + x

    print(string[:-3], end="")
