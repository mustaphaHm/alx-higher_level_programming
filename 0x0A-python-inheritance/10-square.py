#!/usr/bin/python3
"""definition of class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """constructure to initialise size

        Args:
            size (int): a positive integer
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
