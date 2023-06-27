#!/usr/bin/python3
"""In this file we gonna define a square class"""


class Square:
    """Define a square class.

    Attributes:
        __size (int): The size of the square (private).

    Properties:
        size (int): To retrieve and set the size of the square.

    Methods:
        area(): Returns the current square area.
    """

    def __init__(self, size=0):
        """Initialize a square with a given size.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: When size is not an integer.
            ValueError: When size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with #"""
        if self.__size == 0:
            print()
        else:
            for row in range(0, self.__size):
                print("#" * self.__size)
