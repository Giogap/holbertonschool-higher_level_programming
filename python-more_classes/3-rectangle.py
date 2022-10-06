#!/usr/bin/python3
"""
This is a rectangle class
"""


class Rectangle:
    """ This is a rectangle  """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__height + self.__width)
        return perimeter

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        return '\n'.join('#' * self.__width for _ in range(self.__height))
