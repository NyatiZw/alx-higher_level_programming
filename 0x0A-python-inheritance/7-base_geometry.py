#!/usr/bin/python3
"""
Class geometry module
"""


class BaseGeometry:
    """ Public class instances area and integer_validator

    Raise: Exception
    """

    def area(self):
        """ raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ensures value is int greater than 0"""
        if type(value) not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
