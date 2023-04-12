#!/usr/bin/python3
"""
Classes and subclasses
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a square"""
    def __init__(self, size):
        """Instantation of the square"""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """calculates area of a square"""
        return size * size
