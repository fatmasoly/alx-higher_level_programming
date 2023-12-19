#!/usr/bin/python3
"""This module defines the Square class"""


class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of each side of the square.

    Methods:
        __init__(self, size=0): method to initialize the Square instance.
        area(self): Method to compute the area of the square.
        my_print(self): Method to print '#' to stdout.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of each side of square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Gets the size of each side of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        """
        for x in range(self.__size):
            for y in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
