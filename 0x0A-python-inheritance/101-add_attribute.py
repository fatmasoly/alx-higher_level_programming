#!/usr/bin/python3
"""function adds a new attribute to an object """


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if hasattr(obj, '__dict__') or \
       (hasattr(obj, '__slots__') and not getattr(obj, '__slots__')):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
