#!/usr/bin/python3

"""function that prints a square with the character #.
"""


def print_square(size):
    """prints a square with the character #.

    Args:
        size (int): prints a square with the character #.

    Raises:
        TypeError exception with the message size must be an integer
        ValueError exception with the message size must be >= 0

    Returns:
        nothing
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
