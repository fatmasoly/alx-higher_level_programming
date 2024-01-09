#!/usr/bin/python3
"""
This module returns the dictionary description with
simple data structure for JSON serialization of an object:
"""


def class_to_json(obj):
    """
    Convert a Python object into a dictionary.

    Args:
        obj (object): The Python object to be converted.

    Returns:
        dict: A dictionary representation of the input object.
    """
    ret = {}
    for x in dir(obj):
        if not x.startswith("__"):
            ret[x] = obj.__getattribute__(x)
    return ret
