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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "" or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        r = cls(1, 1)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        newList = []
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r", encoding="utf-8") as f:
                data = f.read()
        except FileNotFoundError:
            data = '[]'
        myList = cls.from_json_string(data)
        if myList:
            for dict in myList:
                newList.append(cls.create(**dict))
        return newList
