#!/usr/bin/python3
"""
This function returns a list of object attributes.
"""


def lookup(obj):
    """
    This function returns a list of object attributes.

    Parameters:
        obj (object): The object to inspect.
    Returns:
        list: A list of the object's attributes.

    """
    return dir(obj)
