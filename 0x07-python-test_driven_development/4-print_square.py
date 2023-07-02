#!/usr/bin/python3
"""
Definition of that prints a square with #
"""


def print_square(size):
    """function that prints a square with the character #

    Args:
        size (int, float): the size of the square

    Raises:
        TypeError: when size isn't an integer
        ValueError: when size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * int(size))
