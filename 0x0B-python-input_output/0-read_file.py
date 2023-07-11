#!/usr/bin/python3
"""Definition of a func that reads a file"""


def read_file(filename=""):
    """function that reads a txt file

    Args:
        filename (str, optional): name of the file "".
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
