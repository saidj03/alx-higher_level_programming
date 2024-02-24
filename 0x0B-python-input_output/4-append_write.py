#!/usr/bin/python3
"""
appends a string at the end of a text file (UTF8) and returns the number of
characters added
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    Args:
        filename: name of file to write in
        text: string to be appended
    Returns:
        number of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as myFile:
        return (myFile.write(text))
