#!/usr/bin/python3
"""Definition for a function that add two integers"""


def add_integer(a, b=98):
    """Function that adds two integers

    Args:
        a (int, float): an intger or float number
        b (int, float): an intger or float number. Defaults to 89.

    Raises:
        TypeError: raised when a or b are not integers or floats
    Returns:
        int: the result of a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
