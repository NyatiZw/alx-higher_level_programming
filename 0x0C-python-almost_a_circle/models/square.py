#!/usr/bin/python3
""" Class Square that inherits from rectangle """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Intestaition of Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Square Class """
        self.size = size
        self.x = x
        self.y = y
        super().__init__.__Rectangle(id, x, y, width, height)
