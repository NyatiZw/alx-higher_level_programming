#!/usr/bin/python3
"""
Module 


"""
class BaseGeometry:
    """ Empty class
    
    Raise: Exception
    """

    def __init__area(self):
        raise Exception("area() is not implemented")

    def __init__integer_validator(self, name, value):
        self.name = str(name)
        self.value = value

        if type(value) not int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
