#!/usr/bin/python3
"""function that adds 2 integers
"""


def add_integer(a, b=98):
    """add_integer function

    Args:
        a (int): first operand
        b (int): second operand

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: sum of operands
    """
    if isinstance(a, (int, float)) is False or a == float("inf") or a != a:
        raise TypeError("a must be an integer")
    elif isinstance(b, (int, float)) is False or b == float("inf") or b != b:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
