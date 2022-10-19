#!/usr/bin/python3
"""First Rectangle"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("width must be int")
        if width is not int:
            raise TypeError("width must be integger")
        self.__width = width

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("height must be > 0")
        if height is not int:
            raise TypeError("height must be integger")
        self.__height = height

    @x.setter
    def x(self, x):
        if x < 0:
            raise ValueError("x must be >= 0")
        if x is not int:
            raise TypeError("x must be integger")  
        self.__x = x

    @y.setter
    def y(self, y):
        if y < 0:
            raise ValueError("y must be >= 0")
        if y is not int:
            raise TypeError("y must be integger")
        self.__y = y
