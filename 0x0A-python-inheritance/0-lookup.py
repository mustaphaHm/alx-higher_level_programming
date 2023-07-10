#!/usr/bin/python3
"""Function that return list of available
attributes and methods of an object"""


def lookup(obj):
    """function that lists attributes and methods

    Args:
        obj: an object

    Returns:
        list: list of attributes and methods
    """
    return dir(obj)
