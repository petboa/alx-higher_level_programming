#!/usr/bin/python3
def magic_string():
    s = "BestSchool"
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return ", ".join([s] * magic_string.count)
