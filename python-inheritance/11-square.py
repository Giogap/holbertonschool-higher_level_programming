#!/usr/bin/python3
"""Square #2"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area"""
        return self.size ** 2

    def __str__(self):
        """should print, and str() should return"""
        return "[Square] {}/{}".format(self.size, self.size)
