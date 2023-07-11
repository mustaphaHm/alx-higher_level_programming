#!/usr/bin/python3
"""Definition of function that creates an Object
from a “JSON file"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        obj = json.load(f)
        return obj
