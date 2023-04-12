#!/usr/bin/python3
"""
Class geometry module 
"""


class BaseGeometry:
    """ Public class instance
    
    Raise: Exception
    """

    def __init__area(self):
        raise Exception("area() is not implemented")

    def __init__integer_validator(self, name, value):
        if type(value) not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
