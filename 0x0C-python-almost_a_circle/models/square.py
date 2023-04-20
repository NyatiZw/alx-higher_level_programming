#!/usr/bin/python3
""" Class Square that inherits from rectangle """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Intestaition of Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Square Class
        Args:
            size : size of square
            x: element
            y: member
            id: square id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        _id = self.id
        _x = self.x
        _y = self.y
        _size = self.width, self.height

        return "[Square] + ({}) {}/{} - {}".format(_id, _x, _y, _size)
