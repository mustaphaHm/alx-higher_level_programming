#!/usr/bin/python3
"""In this file we gona define a square"""


class Square:
    """ class that define a square by size

    Attributes:
        __size (int): the size of the square (private)
    """
    def __init__(self, size=0):
        """initialize a square with given size

        Args:
            size (int): the size of the square
        Raises:
            ValueError: if size < 0
            TypeError: if size is not an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
