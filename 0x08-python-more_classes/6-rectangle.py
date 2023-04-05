#!/usr/bin/python3
"""
Defines class Rectangle
"""


class Rectangle:
    """Representation of rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if self.__width ==0 or self.__height == 0:
            return 0
        return (self.__width * 2) * (self.__height * 2)

    def __str__(self):
        """returns a string form of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectang = []
        for i in range(self.__height):
            [rectang.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectang.append("\n")
        return ("".join(recang))

    def __repr__(self):
        """Returns string formof rectangle"""
        rectang = "Rectangle(" + str(self.__width) + ","
        rectang += ", " + str(self.__height) + ")"
        return (rectang)

    def __del__(self):
        """Deletes instance of rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
