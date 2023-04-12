#!/usr/bin/python3
"""
Function to return class


"""

def inherits_from(obj, a_class):
    """Function to return class

    Args:
        obj: object
        a_class: class

    Returns:
        True: if object is class attribute

    """
    if obj is isinstance(obj, a_class):
        return True
    else:
        return False
