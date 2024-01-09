#!/usr/bin/python3
"""
This module for a function that converts a Pyobject into a JSON string.
"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object to its JSON representation as a string.

    Parameters:
    - my_obj: The Python object to be converted to JSON.

    Returns:
    str: A JSON-formatted string representing the input Python object.
    """
    return json.dumps(my_obj)
