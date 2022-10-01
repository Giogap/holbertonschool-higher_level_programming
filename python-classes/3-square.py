#!/usr/bin/python3

""" Class Square """


class Square:
    """ create Square size private"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        self.__size = (self.__size)**2
        return self-__size
