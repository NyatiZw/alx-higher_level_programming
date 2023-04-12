#!/usr/bin/python3
"""
Classes and subclasses
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return ("[Square] " + str(size) + "/" + str(size))
