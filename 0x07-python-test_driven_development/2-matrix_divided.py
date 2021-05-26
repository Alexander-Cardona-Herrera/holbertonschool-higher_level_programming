#!/usr/bin/python3
"""
For this funtion you can't use any type of characters bisides int and float.

Div cant be zero (0)
"""


def matrix_divided(matrix, div):
    """
    Divide the argument matrix by argument div and return a new one.
    """
    x = len(matrix[0])
    str = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != x:
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(row)):
            if type(row[i]) != int and type(row[i]) != float:
                raise TypeError(str)

    new_matrix = [[round((j / div), 2) for j in i] for i in matrix]
    return new_matrix
