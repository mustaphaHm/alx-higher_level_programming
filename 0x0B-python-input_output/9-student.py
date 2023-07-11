#!/usr/bin/python3
"""Definition of class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Func that retrieves a dictionary representation
        of a Student instance """
        return self.__dict__
