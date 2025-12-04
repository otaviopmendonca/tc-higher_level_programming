#!/usr/bin/python3
"""Rectangle module providing a simple Rectangle class."""


class Rectangle:
    """Represents a rectangle defined by width and height."""

    def __init__(self, width=0, height=0):
        """Create a new Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Update the rectangle's width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Update the rectangle's height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Compute and return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a visual representation of the rectangle using '#'."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """Return a reproducible string representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"
