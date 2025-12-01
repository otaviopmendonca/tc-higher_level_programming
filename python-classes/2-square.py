#!/usr/bin/python3
"""
Square class module
This module defines a Square class
"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): Private instance attribute representing the size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square.

        Args:
            size (int): Size of the square (optional, default = 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
