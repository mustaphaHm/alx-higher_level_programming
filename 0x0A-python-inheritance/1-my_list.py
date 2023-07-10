#!/usr/bin/python3
"""definition of class Mylist"""


class MyList(list):
    """Class Mylist inherits from list"""
    def print_sorted(self):
        """fucn that return a sorted list"""
        print(sorted(self))
