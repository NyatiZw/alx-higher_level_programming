#!/usr/bin/python3
import json

"""
Function that rturns the JSON representation of an object

"""


def to_json_string(my_obj):

    """Function to return the json representation of object

    Args:
        my_obj: object

    Return: json object

    """

    return json.dump(my_obj)
