#!/usr/bin/python3

"""
Function that writes an Oject to text file using Json representation


"""
import json


def save_to_json_file(my_obj, filename):

    """Function to write an object in jsonrepresentation

    Args:
        my_obj: object
        filename: name of file

    Return: text file

    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return json.dumps(my_obj)
