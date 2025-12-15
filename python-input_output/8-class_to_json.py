#!/usr/bin/python3
"""Class JSON serialization module."""


def class_to_json(obj):
    """Return a dictionary for JSON serialization."""
    return obj.__dict__
