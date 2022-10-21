#!/usr/bin/python3
""" class Base """


import json
from queue import Empty


class Base:
    """ Doc """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = id
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is Empty or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
