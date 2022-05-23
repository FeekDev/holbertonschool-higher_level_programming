#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == []:
        print("")
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if j != len(matrix) - 1:
                print(matrix[i] ** i [j] ** j, end=" ")

            else:
                print(matrix[i] ** i [j] ** j)

