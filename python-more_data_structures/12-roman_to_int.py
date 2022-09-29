#!/usr/bin/python3
def roman_to_int(roman_string):
    dic_r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    acum = 0
    if ronam_string = "":
        return 0
    for i in range(len(roman_string)):
        if i > 0 and dic_r[roman_string[i]] > dic_r[roman_string[i - 1]]:
            acum += dic_r[roman_string[i]] - 2 * dic_r[roman_string[i - 1]]
        else:
            acum += dic_r[roman_string[i]]
    return acum
