#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Prototype: def matrix_divided(matrix, div):
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message
    matrix must be a matrix (list of lists) of integers/floats.
    Each row of the matrix must be of the same size,
    otherwise raise a TypeError exception with the message
    Each row of the matrix must have the same size.
    div must be a number (integer or float),
    otherwise raise a TypeError exception with the message
    div must be a number.
    div can’t be equal to 0,
    otherwise raise a ZeroDivisionError exception with the message
    division by zero.
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places.
    Returns a new matrix.
    """
    # Check if matrix is a list of lists of integers or floats
    for row in matrix:
        for i in row:
            if not isinstance(row, list) or not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    # Check if each row has the same size
    for row in matrix:
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
