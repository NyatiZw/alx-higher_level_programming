#!/usr/bin/python3
"""Defines a class"""


class Square:
    """Representsa square
    Attributes:
        __size (int): size of sqaure
    """
    def __init__(self, size=0):
        """initialize the square
        Args:
            size (int): size of square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculate the square area
        Returns:
            The area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The sizw
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of a side of thesquare
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must ba an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j  in range(self.__size)]))
