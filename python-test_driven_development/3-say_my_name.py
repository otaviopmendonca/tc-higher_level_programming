#!/usr/bin/python3
"""
Say My Name Module
This module provides a function to print a formatted name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>"

    Args:
        first_name (str): The first name
        last_name (str): The last name, defaults to empty string
   
    Raises:
        TypeError: If first_name or last_name are not strings
    
    Returns: 
        Nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Remove espaço extra quando last_name está vazio
    if last_name == "":
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")
