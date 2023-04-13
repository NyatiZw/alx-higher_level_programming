#!/usr/bin/python3

"""
Function that returns python object as JSON string


"""
import json


def from_json_string(my_str):

    """Function to return the json representation of object

    Args:
        my_obj: object

    Return: json object

    """
    return json.loads(my_str)
