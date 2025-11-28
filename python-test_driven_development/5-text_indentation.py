#!/usr/bin/python3
"""
Text indentation module
This module provides a function that indents the
provided string on specific characters
"""


def text_indentation(text):
    """
    Prints the provided string and indents it by
    adding two new lines when finding '.', ':' or '?'

    Args:
        text: string

    Raises:
        TypeError: if text is not a str object

    Returns:
        Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n\n", end="")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
