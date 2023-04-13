#!/usr/bin/python3

"""
Function that rturns the JSON representation of an object


"""
import json


def to_json_string(my_obj):

    """Function to return the json representation of object

    Args:
        my_obj: object

    Return: json object

    """
    return json.dumps(my_obj)
