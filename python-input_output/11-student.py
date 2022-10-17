#!/usr/bin/python3
"""Student to disk and reload"""


class Student:
    """Class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            nd = {}
            for i in attrs:
                for key, value in self.__dict__.items():
                    if key == i:
                        nd[key] = value
            return nd
        return self.__dict__

    def reload_from_json(self, json):
        self.__dict__.update(json)
    