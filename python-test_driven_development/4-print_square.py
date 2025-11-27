#!/usr/bin/python3
"""
Print square module
This module provides a function to
print a square with the desired number
of #
"""


def print_square(size):
    """
    Prints a square with x number of # in its formation

    Args:
        size: the desired size to your square(integer)

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < than 0

    Returns:
        Nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
