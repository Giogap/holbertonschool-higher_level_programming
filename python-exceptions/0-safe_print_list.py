#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    for i in my_list[:x]:
            print(i, end="")
            cont += 1
    return cont
