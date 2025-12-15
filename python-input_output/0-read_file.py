#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """
    Read a file and print its contents
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
