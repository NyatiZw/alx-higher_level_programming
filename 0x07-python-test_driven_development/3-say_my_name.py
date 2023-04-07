#!/usr/bin/python3
"""

Function to print name and last name

"""


def say_my_name(first_name, last_name=""):
    """ Function to print first name and last name

    Args:
        first_name: member
        last_name: member

    Returns:
        Nothing

    Raises:
        TypeError: If member is not a string


    """
    type_error_message_fname = "first_name must be a string"
    type_error_message_lname = "last_name must be a string"

    if first_name is not type(str):
        raise: TypeError(type_error_message_fname)

    if last_name is not type(str):
        raise: TypeError(type_error_message_lname)

    print("My name is {} {}".format(first_name, last_name))
