#!/usr/bin/python3
def max_integer(my_list=[]):
    aux = 0
    j = 0
    length = len(my_list)
    if length == 0:
        return None
    for i in range(length):
        if my_list[i] > my_list[j + 1]:
            aux = my_list[i]
        else:
            aux = my_list[j + 1]

    return aux

