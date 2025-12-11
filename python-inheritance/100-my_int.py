#!/usr/bin/python3
"""
100-my_int module.
Defines the class MyInt which inherits from int.
"""


class MyInt(int):
    """
    MyInt class inherits from int and inverts the behavior of == and !=.
    """

    def __eq__(self, value):
        """
        Overrides == operator. Returns the result of
        the standard != comparison.
        """
        return not super().__eq__(value)

    def __ne__(self, value):
        """
        Overrides != operator. Returns the result of
        the standard == comparison.
        """
        return not super().__ne__(value)
