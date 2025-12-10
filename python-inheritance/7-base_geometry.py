#!/usr/bin/python3
"""
6-base_geometry module.
Defines the class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """
    A base class for geometry that defines an area method
    """
    def area(self):
        """
        Calculates the area of the geometry.

         Raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value attribute"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
