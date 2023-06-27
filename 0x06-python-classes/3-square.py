#!/usr/bin/python3
"""In this file we gonna define a square class"""


class Square:
    """ define a squre class

    Attributes:
        __size (int): the size of the square (private)
    Methods:
        area(self): returns current square area
    """
    def __init__(self, size=0):
        """ Initialize a square with a given size

        Args:
            size (int): the size of the square
        Raises:
            TypeError: when size in not an integer
            ValueError: when size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ method that returns the current square area"""
    def area(self):
        return self.__size * self.__size
