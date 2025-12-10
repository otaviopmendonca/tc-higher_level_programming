#!/usr/bin/python3
"""
MyList module.
Defines a class that extends list.
"""


class MyList(list):
    """
    Custom list with a method to print a sorted version.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.
        """
        print(sorted(self))
