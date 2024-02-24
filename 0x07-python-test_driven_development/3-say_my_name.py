#!/usr/bin/python3

"""function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name  (str): last name

    Raises:
        TypeError exception
        Message:  first_name must be a string or last_name must be a string

    Returns:
        nothing
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
