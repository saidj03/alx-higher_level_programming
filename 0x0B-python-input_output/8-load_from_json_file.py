#!/usr/bin/python3
"""creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    Args:
        filename: name of file
    """
    with open(filename, encoding='utf-8') as myFile:
        return json.load(myFile)
