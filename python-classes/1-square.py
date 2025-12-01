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

    def __init__(self, size):
        """
        Initializes a new Square.

        Args:
            size: The size of the square.
        """
        self.__size = size
