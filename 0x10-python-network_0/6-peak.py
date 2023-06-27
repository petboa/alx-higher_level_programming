#!/usr/bin/python3

""" function that finds a peak in a list of unsorted integers. """

def find_peak(list_of_integers):
    """find peak value"""
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
