#!/usr/bin/python3
"""
9-rectangle module.
Defines the class Rectangle that inherits from BaseGeometry,
including area calculation and string representation.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle implementing area and string representation.
    """
    
    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns the official string representation of the Rectangle
        """

        return f"[Rectangle] {self.__width}/{self.__height}"
