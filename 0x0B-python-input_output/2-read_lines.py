#!/usr/bin/python3
"""reads n lines of a text file (UTF8) and prints it to stdout"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file (UTF8) and prints it to stdout

    Args:
        filename: name of the file
        nb_lines: number of lines
    """
    with open(filename, encoding="utf-8") as myFile:
        nb_lines = myFile.readlines()
        if nb_lines <= 0 | nb_lines >= len(f_len):
            print(file.read(), end="")
        else:
            for line in MyFile:
                print(line, end="")
