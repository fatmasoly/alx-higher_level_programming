#!/usr/bin/python3
"""
This module defines class `MyList`.
"""


class BaseGeometry:
    """
    This module defines class `MyList`.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This is method for  integer_validator.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
