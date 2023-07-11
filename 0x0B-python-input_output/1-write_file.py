#!/usr/bin/python3
"""Definition of a func that returns
num of charcters written"""


def write_file(filename="", text=""):
    """unc that returns num of charcters written

    Args:
        filename (str, optional): name of the file "".
        text (str, optional): text to be written "".

    Returns:
        int: number of chars written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
