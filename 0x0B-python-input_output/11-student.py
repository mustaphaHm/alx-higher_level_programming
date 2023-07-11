#!/usr/bin/python3
"""Definition of class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Func that retrieves a dictionary representation
        of a Student instance """
        dict = {}
        if type(attrs) is not list:
            return self.__dict__
        else:
            for el in attrs:
                if type(el) is not str:
                    return self.__dict__
            for k in self.__dict__:
                if k in attrs:
                    dict[k] = self.__dict__[k]
        return dict
    
    def reload_from_json(self, json):
        """ replaces all attrs of an instance given json obj """
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
