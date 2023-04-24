#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This function takes two arguments 'a' and 'b' and returns their sum as an integer.
    If either of the arguments is not an integer or a float, it raises a TypeError.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer or a float")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer or a float")
    if isinstance(b, float) and b.is_integer() == False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
