#!/usr/bin/python3
"""Module to find the maximum integer in a list."""
def find_max_integer(list=[]):
    """Function to find and return the maximum integer in a list of integers.
       If the list is empty, the function returns None."""
    if len(list) == 0:
        return None
    max_val = list[0]
    i = 1
    while i < len(list):
        if list[i] > max_val:
            max_val = list[i]
        i += 1
    return max_val
