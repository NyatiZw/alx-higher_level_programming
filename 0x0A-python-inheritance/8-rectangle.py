#!/usr/bin/python3
"""
Classes and Subclasses
"""

BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """Forms a rectangle """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
