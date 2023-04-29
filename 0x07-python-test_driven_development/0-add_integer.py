#!/usr/bin/python3
""" 0-add_integer.py
    add_integer(a, b=98)
"""

def add_integer(a, b=98):
    """ add(a, b=98)
        returns the sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
