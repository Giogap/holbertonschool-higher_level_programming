#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = list(my_list)
    for i in range(len(nw_list)):
        if nw_list[i] == search:
            nw_list[i] = replace
    return nw_list
