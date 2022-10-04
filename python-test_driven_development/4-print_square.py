#!/usr/bin/python3
"""
This is the "4-print_square(size)" module.

The 4-print_square(size) module is function that prints a square.
"""


def print_square(size):
    """ function that prints a square with the character # """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for r in range(0, size):
        for c in range(0, size):
            if c != (size - 1):
                print("#", end="")
            else:
                print("#")
