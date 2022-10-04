#!/usr/bin/python3
"""
This is the "5-text_indentation.py" module.
The function that print 2 new lines after each of these characters.
"""


def text_indentation(text):
    """ function that prints a text with 2 new lines """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char == '.' or char == '?' or char == ':':
            print(char)
            print("")
        else:
            print(char, end="")

