#!/usr/bin/python3
"""
This module provide a func Generates
Pascal's Triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal’s triangle of n.

    Parameters:
    - n (int): The number of rows to generate
    in Pascal's triangle.

    Returns:
    list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """
    Print the Pascal's triangle.

    Parameters:
    - triangle (list): A list of lists representing
    Pascal's triangle.

    Returns:
    None
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
