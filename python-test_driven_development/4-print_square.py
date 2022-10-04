#!/usr/bin/python3
"""
This is the "4-print_square.py" module.

The 4-print_square.py module is function square.
"""


def print_square(size):
    """ Print a square """
    if size is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        if size is float:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
