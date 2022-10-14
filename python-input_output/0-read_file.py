#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """function that reads a text file"""
    with open(filename, encoding='utf-8') as file:
        print(file.read())
