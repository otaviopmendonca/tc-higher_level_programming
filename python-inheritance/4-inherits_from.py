#!/usr/bin/python3
"""
4-inherits_from module.
Contains the inherits_from function which checks for
inheritance (subclassing)excluding the base class itself.
"""


def inherits_from(obj, a_class):
    """
    Returns: True if obj is an instance of a subclass of a_class,
    False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
