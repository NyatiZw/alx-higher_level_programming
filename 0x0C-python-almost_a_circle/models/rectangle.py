#!/usr/bin/python3
""" Class rectangle that inherits from base """

from models.base import Base


class Rectangle(Base):
    """ Intestates a new class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the rectangle class
        Args:
            width: width element of rectangle
            height: height element of rectangle
            x: integer value
            y: integer value
        Raises:
            TypeError: If width or height is not integer
            ValueError: if width or height is less than or equal to zero
            TypeError: if x or y is not an integer
            ValueError: if x or y is less than zero
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def get_width(self):
            return self.__width

        @width.setter
        def set_width(self, width):
            if width <= 0:
                raise ValueError('width must be > 0')
            elif width is not type(int):
                raise TypeError('width must be an integer')
            self.__width = width

        @property
        def get_height(self):
            return self.__height

        @height.setter
        def set_height(self, height):
            if height <= 0:
                raise ValueError('height must be > 0')
            elif height is not type(int):
                raise TypeError("height must be an integer")
            self.__height = height

        @property
        def get_x(self):
            return self.__x

        @x.setter
        def set_x(self, x):
            if x < 0:
                raise ValueError('x must be >= 0')
            elif x is not type(int):
                raise TypeError("x must be an integer")
            self.__x = x

        @property
        def get_y(self):
            return self.__y

        @y.setter
        def set(self, y):
            if y < 0:
                raise ValueError('y must be >= 0')
            elif y is not type(int):
                raise TypeError("y must be an integer")
            self.__y = y
