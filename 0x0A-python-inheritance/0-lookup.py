#!/usr/bin/python3
"""

Function that returns list of available attributes and methods of object
"""

def lookup(obj):
    """ Function that returns object attributes

    Args:
        obj: object element

    Returns:
        Object attributes
    """

    return (dir(obj))
