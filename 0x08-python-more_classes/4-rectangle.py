#!/usr/bin/python3

"""Defines class Rectangle"""


class Rectangle:
    """Representation of rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        Raises:
            TypeError: if not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """getter for width"""
            return self.__width

        @width.setter
        def width(self, value):
            """setter for width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be an >= 0")
            self.__width = value

            @property
            def height(self):
                """getter for height"""
                return self.__height

            @height.setter
            def height(self, value):
                """setter for height"""
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value

            def area(self):
                """returns area of rectangle"""
                return self.__width * self.__height

            def perimeter(self):
                """returns perimeter of rectangle"""
                if self.__width == 0 or self.__height == 0:
                    return 0
                return (self.__width * 2) * (self.__height * 2)

            def __str__(self):
                """returns a string"""
                string = ""
                if self.__width != 0 and self.__height != 0:
                    string += "\n".join("#" * self.__width
                            for j in range(self.__height))
                    return string
