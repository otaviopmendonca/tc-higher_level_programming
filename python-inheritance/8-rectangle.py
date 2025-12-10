#!/usr/bin/python3
"""
8-rectangle module.
Defines the class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle,
    inheriting validation logic from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
