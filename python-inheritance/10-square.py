#!/usr/bin/python3
"""
10-square module.
Defines the class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square with size.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return square area"""
        return self.__size * self.__size
    