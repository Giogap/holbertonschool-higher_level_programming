#!/usr/bin/python3
""" class Base """

__nb_objects = 0


class Base:
    """ Doc """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = id
            __nb_objects += 1
            id = __nb_objects