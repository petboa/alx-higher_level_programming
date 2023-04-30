#!/usr/bin/python3
"""Module for a function that prints a name."""


def print_name(first_name, last_name=""):
    """Prints the first and last name provided as arguments.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If either of the arguments is not a string.
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("Both arguments must be strings.")
        
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
