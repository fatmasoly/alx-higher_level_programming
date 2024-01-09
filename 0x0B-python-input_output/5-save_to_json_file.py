#!/usr/bin/python3
"""
This module for a function that writes an Object to a
text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using
    a JSON representation.

    Parameters:
    - my_obj: The Python object to be written to the file.
    - filename (str): The name of the file to which
    the Python object will be saved.

    Returns:
    None
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
