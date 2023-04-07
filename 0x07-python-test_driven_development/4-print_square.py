#!/usr/bin/python3

"""
Function that prints a square

"""


def print_square(size):

    """
    Function that prints a square

    Args:
        size: size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero

    Returns:
        Nothing

    """

    if size < 0:
        raise ValueError("size must be >= 0")

    if size not isinstance(size, int):
        raise TypeError("size must be an integer")

    for j in range(size):
        print("#" * size)
