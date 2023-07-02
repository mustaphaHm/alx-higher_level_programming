#!/usr/bin/python3
""" Definition of a function that
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): the text to be indented

    Raises:
        TypeError: when text is not str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    text = text.replace(". ", ".").replace(": ", ":").replace("? ", "?")
    for c in text:
        result += c
        if c in [".", ":", "?"]:
            result += "\n\n"
    print(result)
