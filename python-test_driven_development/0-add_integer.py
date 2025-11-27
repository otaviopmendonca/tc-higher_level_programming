#!/usr/bin/python3
"""
This module provides the add_integer function.

It adds two integers and returns the result.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: first number
        b: second number (default: 98)

    Returns:
        int: the sum of a and b after casting to int

    Raises:
        TypeError: if a or b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
