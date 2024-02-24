#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: file to read
    """
    with open(filename, encoding="utf-8") as MyFile:
        for line in MyFile:
            print(line, end="")
