#!/usr/bin/python3

class Base:
    """ First class named Base
    Attributes:
        __nb_objects : private class integer attribute
    """

    __nb_objects = 0


    def __init__(self, id=None):
        """ Function to initialize a base
        Args:
            id : integer value of base id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
