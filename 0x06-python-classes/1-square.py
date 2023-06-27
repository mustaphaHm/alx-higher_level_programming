#!/usr/bin/python3
"""In this file we gonna define a square class"""


class Square:
    """A class that defines a square

    Attributes:
        __size (int) : the size of the square (private)
    """
    def __init__(self, size):
        """Initialize a square with a given size

        Args:
            size (int) : the size of the square
        """
        self.__size = size
