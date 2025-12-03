#!/usr/bin/python3
"""Square class with numeric size, area method and comparison operators."""


class Square:
    """
    Defines a square with a private size attribute, including validation,
    area calculation and comparison operators based on square area.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int or float, optional): Length of each side of the square.
                                           Must be a non-negative number.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is < 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation for numbers (int or float)."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the current area of the square.

        Returns:
            int or float: size squared.
        """
        return self.__size * self.__size

    # Comparison operators based on area
    def __eq__(self, other):
        """Equality comparison based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Non-equality comparison based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less-than comparison based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less-or-equal comparison based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater-than comparison based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater-or-equal comparison based on area."""
        return self.area() >= other.area()
