#!/usr/bin/python3

from .base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        def get_width(self):
            return self.__width

        def set_width(self, width):
            if width <= 0:
                raise ValueError('width must be > 0')
            elif width is not type(int):
                raise TypeError('width must be an integer')
            self.__width = width

        def get_height(self):
            return self.__height

        def set_height(self, height):
            if height <= 0:
                raise ValueError('height must be > 0')
            elif height is not type(int):
                raise TypeError("height must be an integer")
            self.__height = height

        def get_x(self):
            return self.__x

        def set_x(self, x):
            if x < 0:
                raise ValueError('x must be >= 0')
            elif x is not type(int):
                raise TypeError("x must be an integer")
            self.__x = x

        def get_y(self):
            return self.__y

        def set(self, y):
            if y < 0:
                raise ValueError('y must be >= 0')
            elif y is not type(int):
                raise TypeError("y must be an integer")
            self.__y = y
