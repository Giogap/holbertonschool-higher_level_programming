#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module is function that adds 2 integers, add_integer(a, b).
"""


def matrix_divided(matrix, div):
    if matrix is not int or matrix is not float:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix):
        if len(matrix[0] != len(matrix[i+1]:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) in not in and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
