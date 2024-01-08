#!/usr/bin/python3
"""
This module provides functions for checking the type
and class inheritance relationships of objects.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise, False.

    Parameters:
    - obj: Any Python object
        The object to check.
    - a_class: class
        The specified class to check against.

    Returns:
    - bool
        True if the object is an instance of a class that inherited
        from the specified class; otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
