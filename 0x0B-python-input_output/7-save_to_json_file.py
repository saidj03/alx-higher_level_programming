#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
        my_obj: object to be written
        filename: name of file where object will be written
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return myFile.write(json.dumps(my_obj))
