#!/usr/bin/python3
"""First Rectangle"""
Base = __import__('base').Base


class Rectangle:
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self):
        pass

    @height.setter
    def wheight(self):
        pass

