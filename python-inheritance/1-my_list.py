#!/usr/bin/python3
"""Class MyList"""


class MyList(list):
    """Class MyList that inherits from list"""
    def print_sorted(self):
        """Print list sorted"""
        print (sorted(self))
