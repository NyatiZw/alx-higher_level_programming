#!/usr/bin/python3
"""
Defines class Rectangle
"""


class Rectangle:
    """Representation of rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        rect_str = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            rect_str += str(self.print_symbol) * self.width
            if i + 1 < self.__height:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """Returns string formof rectangle"""
        rect_str = "Rectangle(" + str(self.__width) + ","
        rect_str += str(self.__height) + ")"
        return (rect_str)

    def __del__(self):
        """Deletes instance of rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
