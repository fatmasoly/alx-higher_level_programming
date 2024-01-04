#!/usr/bin/python3
"""
N-Queens Solver

Usage:
    ./nqueens.py N

Solves the N-Queens problem by placing N non-attacking
queens on an N×N chessboard.

Arguments:
    N (int): The size of the chessboard and the number of queens.

Requirements:
    - The user must provide a valid integer N
    (greater or equal to 4) as a command-line argument.

Output:
    Prints every possible solution to the N-Queens
    problem, with one solution per line
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if placing a queen at a specific position is safe.

    Args:
        board (list): The chessboard.
        row (int): The current row.
        col (int): The current column.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe, False otherwise.
    """
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_solution(board):
    """
    Print the current solution.

    Args:
        board (list): The chessboard with queens placed.
    """
    n = len(board)
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def solve_nqueens(board, col, n):
    """
    Solve the N-Queens problem using backtracking.

    Args:
        board (list): The chessboard.
        col (int): The current column.
        n (int): The size of the chessboard.
    """
    if col >= n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n)
            board[i][col] = 0  # Backtrack


def nqueens(n):
    """
    Main function to solve the N-Queens problem.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Raises:
        ValueError: If N is not an integer or is less than 4.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
