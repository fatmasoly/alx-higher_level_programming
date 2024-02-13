#!/usr/bin/python3
"""
This module for a function that reads text to a file.
"""


def read_file(filename=""):
    """
    Reads the contents of a file and prints them to the console.

    Parameters:
    - filename (str): The name of the file to be read.
    Default is an empty string.

    Returns:
    None
    """
    with open(filename, "r") as fl:
        print(fl.read(), end="")
