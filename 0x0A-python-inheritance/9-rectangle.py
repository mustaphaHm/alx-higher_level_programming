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
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """return the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print [Rectangle] width/height"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
