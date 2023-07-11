#!/usr/bin/python3
"""Definition of function that returns an object
(Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """func that return object"""

    return json.loads(my_str)
