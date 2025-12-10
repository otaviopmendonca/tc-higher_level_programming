#!/usr/bin/python3
"""
2-is_same_class module.
Contains the is_same_class function which checks 
for exact object type equality.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    This function only returns True if the object's type is identical
    to the specified class, excluding subclasses.

    Args:
        obj: The object to check.
        a_class: The class to compare the object's type against.

    Returns:
        True if the type of obj is exactly a_class, False otherwise.
    """
    return type(obj) is a_class
