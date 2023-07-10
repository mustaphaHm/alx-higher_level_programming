#!/usr/bin/python3
"""definition of class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """constructure to initialise width and height

        Args:
            width (int): the width
            height (int): the height_
        """
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height
