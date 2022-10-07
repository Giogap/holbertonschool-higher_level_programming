#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0

    def __init__(self, width = 0, height = 0):
        """Initialize"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        print_symbol = "#"

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        string = ''
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            string += "\n"
        return string[:-1]

    def __repr__(self):
        return ('Rectangle(' + str(self.__width) + ', ' +
                str(self.__height) + ')')

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
