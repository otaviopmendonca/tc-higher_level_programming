#!/usr/bin/python3
"""
101-add_attribute module.
Defines the add_attribute function that safely adds a new attribute 
to an object if possible.
"""


def add_attribute(obj, name, value):
    """
    Add attribute to object or raise TypeError
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
