#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
       width (int): The width of the rectangle.
       height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        The constructor for the Rectangle class.

        Parameters:
           width (int): The width of the rectangle.
           height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        The width of the rectangle.

        Returns:
           int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Parameters:
           value (int): The new width of the rectangle.

        Raises:
           TypeError: If the width is not an integer.
           ValueError: If the width is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        The height of the rectangle.

        Returns:
           int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Parameters:
           value (int): The new height of the rectangle.

        Raises:
           TypeError: If the height is not an integer.
           ValueError: If the height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
           int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
           int: The perimeter of the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Returns:
           str: A string representing the rectangle.
        """
        st = ""
        if self.height == 0 or self.width == 0:
            return st
        for i in range(self.height):
            for j in range(self.width):
                st += "#"
            if i != (self.height - 1):
                st += "\n"
        return st

    def __repr__(self):
        """
        Return a string representation of the
        rectangle suitable for reproduction.

        Returns:
           str: A string representation of the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"
