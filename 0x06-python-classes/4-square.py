#!/usr/bin/python3
"""Define Class"""


class Square:
    """Represent a square
    Attributes:
        __size(int): size of square
    """
    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of sqaure
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculate square area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """gets size
        Returns:
            Size of square
        """
        return self.__size

    @size.set
    def size(self, value):
        """sets size
        Args:
            value (int): size
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
