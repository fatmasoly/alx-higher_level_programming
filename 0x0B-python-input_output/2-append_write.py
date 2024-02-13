#!/usr/bin/python3
"""
This module for a function that appends text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends the specified text to a file.

    Parameters:
    - filename (str): The name of the file to which the text
    will be appended. Default is an empty string.
    - text (str): The text to be appended to the file.
    Default is an empty string.

    Returns:
    int: The number of characters appended to the file.
    """
    with open(filename, "a") as f:
        f.write(text)
        return len(text)
