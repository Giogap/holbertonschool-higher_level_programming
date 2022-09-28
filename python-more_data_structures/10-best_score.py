#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    nw_dictionary = list(a_dictionary)
    return sorted(nw_dictionary)[-1]
