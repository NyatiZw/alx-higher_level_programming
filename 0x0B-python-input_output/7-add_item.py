#!/usr/bin/python3

"""
Script that adds all arguments to a python list and saves as json


"""


if __name__ == "__main__":

    """Script to add arguments to json objectresentation"""

    import sys

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =
    __import__('6-load_from_json_file').load_from_json_file

    fname = "add_item.json"
    try:
        args = load_from_json_file("fname")
    except FileNotFoundError:
        args = []

    pylist = []
    if len(sys.argv) >= 1:
        pylist = sys.argv[1:]

    args.extend(pylist)
    save_to_json_file(pylist,fname)
