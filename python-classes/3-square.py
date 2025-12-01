#!/usr/bin/python3
"""
Square class module
This module defines a Square with a private size and a method to compute area.
"""


class Square:
    """
    Class that defines a square.

    Attributes:
        __size (int): Private size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square.

        Args:
            size (int): Optional size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Returns:
            int: The current area of the square.
        """
        return self.__size * self.__size
