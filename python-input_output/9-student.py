#!/usr/bin/python3
"""Student module."""


class Student:
    """Student data model."""

    def __init__(self, first_name, last_name, age):
        """Initialize student data."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation."""
        return self.__dict__
