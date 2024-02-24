#!/usr/bin/python3
"""
writes a string to a text file (UTF8) and returns the number of characters
written
"""


def write_file(filename="", text=""):
    """ writes a string to a text file
    Args:
        filename: name of file
        text: string to be written
    Returns:
        number of written characters
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        return (myFile.write(text))
