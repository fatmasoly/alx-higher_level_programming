#!/usr/bin/python3
"""
This module provides functions for checking type and class relationship
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or a subclass thereof.

    Parameters:
    - obj: Any Python object
        The object to check.
    - a_class: class
        The specified class or a superclass to check against.

    Returns:
    - bool
        True if the object is an instance of the specified class
        or a subclass thereof; otherwise, False.
    """
    return isinstance(obj, a_class)
