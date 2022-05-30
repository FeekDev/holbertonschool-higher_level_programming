#!/usr/bin/python3
"""
This module function that
divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Parameter: Matrix send the list of list and div send the divisor
    """
    i = 0
    j = 0
    string_type = "matrix must be a matrix (list of lists) of integers/floats"
    string_len = "Each row of the matrix must have the same size"
    new_matrix = [
        [0, 0, 0],
        [0, 0, 0]
        ]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(string_type)
            elif len(new_matrix[i]) != len(matrix[i]):
                raise TypeError(string_len)
            elif type(div) not in [int, float]:
                raise TypeError("div must be a number")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            new_matrix[i][j] = float("{0:.2f}".format(matrix[i][j]/div))
            if type(new_matrix[i][j]) not in [int, float]:
                raise TypeError(string_type)

    return new_matrix
