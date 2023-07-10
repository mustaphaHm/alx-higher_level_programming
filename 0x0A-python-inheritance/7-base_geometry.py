#!/usr/bin/python3
"""definition of class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """function area

        Raises:
            Exception: func not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates a value

        Args:
            name (string): name of variable
            value (int): the value

        Raises:
            TypeError: when value is not an integer
            ValueError: when value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
