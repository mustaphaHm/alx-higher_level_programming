#!/usr/bin/python3
"""Definition of class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """classe Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        # Calling the class base contructor
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Getters
    @property
    def width(self):
        """Get the width"""
        return self.__width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @property
    def x(self):
        """Get x"""
        return self.__x

    @property
    def y(self):
        """Get y"""
        return self.__y

    # Setters
    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
