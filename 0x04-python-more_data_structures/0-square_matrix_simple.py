#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        new_row = []

        for ele in row:
            sqr = ele * ele
            new_row.append(sqr)

        new_matrix.append(new_row)

    return new_matrix
