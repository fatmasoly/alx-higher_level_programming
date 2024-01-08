#!/usr/bin/python3
"""
Module: rectangle

This module defines the Rectangle class,
which is a subclass of BaseGeometry.
It represents a rectangle and provides methods for
validation and access to its dimensions.

Classes:
- Rectangle(BaseGeometry)
    Represents a rectangle and inherits from
    the BaseGeometry class.

Attributes:
- __width: int
    The width of the rectangle.
- __height: int
    The height of the rectangle.

Methods:
- __init__(self, width, height)
    Initializes a new instance of the Rectangle class
    with the specified width and height.
"""


class Rectangle(BaseGeometry):
    """
    Rectangle class represents a rectangle and inherits
    from the BaseGeometry class.

    Attributes:
    - __width: int
        The width of the rectangle.
    - __height: int
        The height of the rectangle.

    Methods:
    - __init__(self, width, height)
        Initializes a new instance of the Rectangle class
        with the specified width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class
        with the specified width and height.

        Parameters:
        - self: Rectangle
            The instance of the Rectangle class.
        - width: int
            The width of the rectangle.
        - height: int
            The height of the rectangle.

        Returns:
        - None
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
