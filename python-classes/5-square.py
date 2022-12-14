#!/usr/bin/python3

""" Class Square """


class Square:
    """ create Square size private"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        area = (self.__size) * (self.__size)
        return area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
