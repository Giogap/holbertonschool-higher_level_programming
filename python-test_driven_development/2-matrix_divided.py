#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module is function that adds 2 integers, add_integer(a, b).
"""


def matrix_divided(matrix, div):
    """ Return new matriz with the division of elelments """
    nw_matrix = []
    for fila in matrix:
        if all(isinstance(x, (int, float)) for x in fila) is False:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(fila, (list)) for fila in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    for fila in matrix:
        if len(matrix[0]) != len(fila):
            raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        nw_matrix.append(list(map(lambda x: round(x/div, 2), i)))
    return nw_matrix
