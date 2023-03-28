#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Class representing a square"""

    def __init__(self, size=0):
        """Initializing square
        Args:
            size: size
        Returns:
            TypeError
            ValueError
        """

        self.size = size

    def area(self):
        """
        Calculates area of square
        Returns: The size of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
