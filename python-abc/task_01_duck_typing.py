#!/usr/bin/python3
"""
Task 1: Shapes, Interfaces, and Duck Typing
Implements Shape ABC and concrete subclasses (Circle, Rectangle),
showcasing interface enforcement and duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class (ABC) for geometric shapes."""

    @abstractmethod
    def area(self):
        """
        Calculates and returns the shape's area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates and returns the shape's perimeter.
        """
        pass


class Circle(Shape):
    """
    Implementation of a circle shape
    """

    def __init__(self, radius):
        """
        Initializes the circle with Radius
        """
        self.__radius = abs(radius)

    def area(self):
        """
        Returns the area
        """
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """
        Returns the perimeter (circumference)
        """
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Implementation of a rectangle shape
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the perimeter.
        """
        return 2 * (self.__height + self.__width)


def shape_info(obj):
    """
    Prints the area and perimeter of any object using Duck Typing.
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
