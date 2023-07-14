#!/usr/bin/python3
"""Definition of classe Base that manage teh attribute id"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructur

        Args:
            id (int, optional): intger parameter
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
