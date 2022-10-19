#!/usr/bin/python3
""" class Base """



class Base:
    """ Doc """
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = id
            __nb_objects += 1
            id = __nb_objects