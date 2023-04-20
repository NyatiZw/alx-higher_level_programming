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

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, val):
        """ size setter """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """ Updating square
        Args:
            *args : Attribute values
                - arg_1 represents id attribute
                - arg_2 represents size
                - arg_3 represents x
                - arg_4 represents y
            **kwargs (dict): Key/value argument pairs.
        """
        if args is not None and len(args) is not 0:
            _list = ['id', 'size', 'x', 'y']
            for i in range(len(arge)):
                if _list[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, _list[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary  of attributes """
        list_attributes = ['id', 'size', 'x', 'y']
        dictionary_result = {}

        for key in list_attributes:
            if key == 'size':
                dictionary_result[key] = getattr(self, 'width')
            else:
                dictionary_result[key] = getattr(self, key)

        return dictionary_result
