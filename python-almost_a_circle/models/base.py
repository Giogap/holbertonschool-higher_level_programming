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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is Empty or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """"""
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string is Empty:
            return []
        return json.loads(json_string)

    @classmethod
    def update(cls, **dictionary):
        if cls.__name__ == "Square":
            dummy = cls(1, 1)
        