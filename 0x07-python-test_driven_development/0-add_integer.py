#!/bin/python3
"""

Function that adds two numbers

"""


def add_integer(a, b=98):
    """ Function that adds two integers

    Args:
        a: first integer value
        b: second integer value

    Returns:
        The sum of the args

    Raises:
        TypeError: If a or b not int

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
