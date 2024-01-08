#!/usr/bin/python3


def print_square(size):
    """
    Prints a square with the character '#' of the specified size.

    Args:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than 0 or if size is a float less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0 or (isinstance(size, float) and size < 0):
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
