#!/usr/bin/python3
def roman_to_int(roman_string):
    dic_r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    acum = 0
    romano = list(roman_string)
    for i in range(len(roman_string)):
        if i > 0 and dic_r[romano[i]] > dic_r[romano[i - 1]]:
            acum += dic_r[romano[i]] - 2 * dic_r[romano[i - 1]]
        else:
            acum += dic_r[romano[i]]
    return acum
