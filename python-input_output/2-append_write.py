#!/usr/bin/python3
"""File append module."""


def append_write(filename="", text=""):
    """Append text to a file and return character count."""
    with open(filename, "a") as file:
        file.write(text)
    return len(text)
