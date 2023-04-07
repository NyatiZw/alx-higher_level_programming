#!/usr/bin/python3
"""


Function to divide integers

"""


def matrix_divided(matrix, div):
    """ Function to divide some integers

    Args:
        matrix: list of lists
        div: int tto divide with

    Returns:
        New matrix

    Raises:
        TypeError: if matrix is not a list
                   if elements aren't integers
                   if div is not an integer/float
                   if list is not same size

        ZeroDivisionError: if div is zero


    """

    if not type(div) in (int, float):
        rasie TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    error_type_message = "matrix must be a matrix (list of list) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(error_type_message)

    length = 0
    error_size_message = "Each row of the matrix must have the same size"

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(error_type_message)

        if length != 0 and len(elements) != length:
            raise TypeError(error_size_message)

        for number in elements:
            if not type(number) in (int, float):
                raise TypeError(error_type_message)

        length = len(elements)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
