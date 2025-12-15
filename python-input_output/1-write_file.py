#!/usr/bin/python3
"""File writing module."""


def write_file(filename="", text=""):
    """Write text to a file and return character count."""
    with open(filename, 'w') as file:
        file.write(text)
    return len(text)
