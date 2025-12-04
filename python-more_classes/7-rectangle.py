#!/usr/bin/python3
"""Simple Rectangle class module."""


class Rectangle:
    """Rectangle defined by width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Return width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter or 0 if invalid."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return printable rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.width for _ in range(self.height))

    def __repr__(self):
        """Return formal representation."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Notify deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
