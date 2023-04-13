#!/usr/bin/python3

"""
Script that adds all arguments to a python list and saves as json


"""
import json
import sys


if __name__ == "__main__"

    """Script to add arguments to json objectresentation"""

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    fname = ""

    pylist = []
    if len(sys.argv) >= 1:
        pylist = sys.argv[1:]

    fname.extend(pylist)
    save_to_json_file(pylist, fname)
