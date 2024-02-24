#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """class that defines a student with attributes name and age"""

    def __init__(self, first_name, last_name, age):
        """instantiation of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method to retrieve a dictionary representation of student"""
        return(self.__dict__)
