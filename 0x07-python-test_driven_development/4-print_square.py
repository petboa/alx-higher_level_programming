#!/usr/bin/python3
"""Defines a function that prints a square with the # character."""


def print_square(size):
    """Prints a size x size square made of the # character.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than or equal to 0.

    Returns:
        None
    """
    if not isinstance(size, int) or size is None:
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be greater than 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
