#!/usr/bin/python3
"""
11-square module.
Defines the class Square that inherits from Rectangle, 
with custom string representation.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Returns the square area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return string representation of square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
