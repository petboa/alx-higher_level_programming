#!/usr/bin/python3
"""
This function prints a person's name.
"""

def print_name(first_name, last_name=""):
    """
    Prints out "My name is <first name> <last name>".

    Args:
        first_name (str): The person's first name.
        last_name (str, optional): The person's last name. Defaults to "".

    Raises:
        TypeError: If either argument is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
