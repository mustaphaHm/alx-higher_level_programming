#!/usr/bin/python3
"""In this file we gonna define a square class"""


class Square:
    """Define a square class.

    Attributes:
        __size (int): The size of the square (private).
        __position (int): The postion of the square (private).

    Properties:
        size (int): To retrieve and set the size of the square.
        position: the position of the square

    Methods:
        area(): Returns the current square area.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a given size.

        Args:
            size (int): The size of the square.
            position: the position of the square
        Raises:
            TypeError: When size is not an integer.
            ValueError: When size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the tuple of the square."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
