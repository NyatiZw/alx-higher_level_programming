#!/usr/bin/python3

"""Function that prints a square"""


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

    for i in range(size):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif size not isinstance(size, int):
            raise TypeError("size must be an integer")

        print("#" * size)
