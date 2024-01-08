#!/usr/bin/python3
"""
Module: base_geometry

This module defines the BaseGeometry class, which serves as
a base class for geometry-related operations.

Classes:
- BaseGeometry
    A base class for geometry operations. It provides a placeholder
    method for 'area' and a method for validating integers.

Methods:
- BaseGeometry.area(self)
    Raises an exception indicating that the 'area' method is not
    implemented This method serves as a placeholder
    for subclasses to provide their own implementation.

- BaseGeometry.integer_validator(self, name, value)
    Validates if the given value is an integer and greater than 0
    Raises appropriate exceptions for invalid values.

Note: This module provides a foundation for more
specific geometry-related classes.
"""


class BaseGeometry:
    """
    BaseGeometry class serves as a base class for
    geometry-related operations.

    Methods:
    - area(self)
        Raises an exception indicating that the 'area' method is not
        implemented. This method serves as a placeholder
        for subclasses to provide their own implementation.

    - integer_validator(self, name, value)
        Validates if the given value is an integer and greater than 0
        Raises appropriate exceptions for invalid values.
    """

    def area(self):
        """
        Placeholder method for 'area'. Raises an exception indicating
        that the 'area' method is not implemented.

        Parameters:
        - self: BaseGeometry
            The instance of the BaseGeometry class.

        Returns:
        - None

        Raises:
        - Exception
            Indicates that the 'area' method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the given value is an integer and greater than 0.
        Raises appropriate exceptions for invalid values.

        Parameters:
        - self: BaseGeometry
            The instance of the BaseGeometry class.
        - name: str
            The name of the value being validated.
        - value: Any
            The value to be validated.

        Returns:
        - None

        Raises:
        - TypeError
            If the value is not an integer.
        - ValueError
            If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
