#!/usr/bin/python3
"""
This module for a function that writes text to a file.
"""


def write_file(filename="", text=""):
    """
    Writes the specified text to a file.

    Parameters:
    - filename (str): The name of the file to be
    written. Default is an empty string.
    - text (str): The text to be written to the file.
    Default is an empty string.

    Returns:
    int: The number of characters written to the file.
"""
    with open(filename, "w") as f:
        f.write(text)
        return len(text)
