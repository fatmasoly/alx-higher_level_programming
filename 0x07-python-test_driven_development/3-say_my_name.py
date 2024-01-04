#!/usr/bin/python3
"""
This module defines a function to print a person's full name.

The function `say_my_name` takes two parameters, `first_name` and `last_name`,
and prints the formatted full name using the provided values.

Usage:
    say_my_name(first_name, last_name="")

Parameters:
    first_name (str): The person's first name.
    last_name (str, optional): The person's last name. Defaults to "".

Raises:
    TypeError: If first_name or last_name is not a string.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints the person's full name.

    Args:
        first_name (str): The person's first name.
        last_name (str, optional): The person's last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
