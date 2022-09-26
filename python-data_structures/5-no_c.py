#!/usr/bin/python3
def no_c(my_string):
    nw_st = ""
    for i in my_string:
        if i != "c" and i != "C":
            nw_st += i
    return nw_st
