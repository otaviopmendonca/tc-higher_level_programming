#!/usr/bin/python3
"""Square class with size, position, area and print behavior"""


class Square:
    """
    Defines a square with private size and position attributes,
    including validation, area calculation and printable output.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance.

        Args:
            size (int, optional): Length of each side of the square.
            position (tuple, optional): Tuple of 2 positive integers
                                        representing horizontal and
                                        vertical offsets.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is < 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """
        Return the current area of the square.

        Returns:
            int: size squared.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using '#' with respect to position.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Vertical offset
        print("\n" * self.__position[1], end="")

        for _ in range(self.__size):
            # Horizontal offset + square line
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Return printable string representation of the square.
        Behaves like my_print() but returns the string instead of printing.
        """
        if self.__size == 0:
            return ""

        lines = []
        # Vertical offset
        for _ in range(self.__position[1]):
            lines.append("")

        # Square body
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)
