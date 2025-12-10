#!/usr/bin/python3
"""
3-is_kind_of_class module.
Contains the is_kind_of_class function
which checks for type or inherited type.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of the specified class or
    a class that inherited from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object's type
        or inheritance against.

    Returns:
        True if obj is an instance of a_class
        or a class inherited from a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
