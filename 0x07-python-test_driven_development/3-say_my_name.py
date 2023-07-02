#!/usr/bin/python3
"""
Definition of a function that prints first and last name
"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>

    Args:
        first_name (str): the first name
        last_name (str, optional): the last name. Defaults to "".

    Raises:
        TypeError: when the first or last name aren't strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
