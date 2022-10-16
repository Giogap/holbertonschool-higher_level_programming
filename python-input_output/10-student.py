#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) != list:
            return self.__dict__