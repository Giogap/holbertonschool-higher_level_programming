#!/usr/bin/python3
def common_elements(set_1, set_2):
    for i in range(len(set_1)):
        if set_1[i] == set_2[i]:
            return set_1[i]
