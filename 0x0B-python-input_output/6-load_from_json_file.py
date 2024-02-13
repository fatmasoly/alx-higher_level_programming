#!/usr/bin/python3
"""
This module for a function that
creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file to be loaded.

    Returns:
    obj: A Python object representing the data stored in the JSON file.
    """
    with open(filename, "r") as file:
        return json.load(file)
