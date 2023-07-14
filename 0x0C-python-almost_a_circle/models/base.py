#!/usr/bin/python3
"""Definition of classe Base that manage teh attribute id"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write json string of list_objs to a file """
        file_name = cls.__name__ + ".json"
        if list_objs:
            listObj = [obj.to_dictionary() for obj in list_objs]
            toWrite = cls.to_json_string(listObj)
        else:
            toWrite = "[]"
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(toWrite)
