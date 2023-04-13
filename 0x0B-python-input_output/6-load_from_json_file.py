#!/usr/bin/python3

"""
Function that creates an Object from a JSON file


"""
import json


def load_from_json_file(filename):

    """Function to write an object in jsonrepresentation

    Args:
        my_obj: object
        filename: name of file

    Return: text file

    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        return json.load(filename, f)
