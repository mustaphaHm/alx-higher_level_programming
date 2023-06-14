#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMtr = []
    for row in matrix:
        newMtr.append(list(map(lambda x: x * x, row)))
    return newMtr
