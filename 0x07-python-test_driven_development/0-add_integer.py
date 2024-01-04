#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Prototype: def add_integer(a, b=98):
    a and b must be integers or floats,
    otherwise raise a TypeError exception
    with the message a must be an integer or b must be an integer.
    a and b must be first casted to integers if they are float.
    Returns an integer: the addition of a and b.
    """
    # Check if a and b are an integer or float
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
