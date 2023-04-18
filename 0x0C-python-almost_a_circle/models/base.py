#!/usr/bin/python3
""" Define class model base """


class Base:
    """ First class named Base
    Attribute:
        __nb_objects: number of bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Function to initialize a base
        Args:
            id: id element
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
