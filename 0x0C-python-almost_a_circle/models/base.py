#!/usr/bin/python3
"""module that creates a class called Base"""

import json


class Base:
    """This class will be the “base” of all other classes in this project.
    Its goal is to manage the id attribute in all your future classes and
    to avoid duplicating the same code.

    Attributes:
        __nb_objects = 0: private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """"class constructor
        Attributes:
            id: integer, public instance attribute
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """ static method returns the JSON string representation of
        list_dictionaries

        Attributes:
            list_dictionaries: list of dictionaries
        Returns:
            json string
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation of
        list_objs to a file
        
        Attributes:
            cls: class name
            list_objects: list_objs is a list of instances that inherits of Base
        """
        json_filename = cls.__name__ + ".json"
        list_string = []
        with open(json_fiile_name, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")        
            else:
                for i in list_objs:
                    list_string.append(cls.to_dictionary(i))
            json_file.write(cls.to_json_string(list_string))
