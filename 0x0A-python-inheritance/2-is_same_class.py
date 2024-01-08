#!/usr/bin/python3
"""
The module defines a class `MyList`.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an
    instance of the specified class; otherwise False.

    Parameters:
    - obj: Any Python object
        The object to check.
    - a_class: class
        The specified class to compare against.

    Returns:
    - bool
        True if the object is an instance of the
        specified class; otherwise, False.
    """

    return type(obj) is a_class
