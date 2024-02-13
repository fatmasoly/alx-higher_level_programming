#!/usr/bin/python3
"""
This module for a function that converts a JSON string into a Pyobject
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON-formatted string to a Python object.

    Parameters:
    - my_str (str): The JSON-formatted string to be converted.

    Returns:
    obj: A Python object representing the data from the input JSON string.
    """
    return json.loads(my_str)
