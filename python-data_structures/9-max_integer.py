#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    for i in my_list:
        if i > length:
            length = i
    return length
