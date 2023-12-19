#!/usr/bin/python3
"""This module defines the Square class"""


class Square:
    """
    This class represents a square.

    Attributes:
        size (int): The size of each side of the square.
        position (tuple): The position of the square
        in the x-axis and y-axis.

    Methods:
        __init__(self, size=0, position=(0, 0)):
        Constructor method to initialize the Square instance.
        area(self): Method to compute the area of the square.
        my_print(self): Method to print the square
        with the character '#' to stdout.

    Raises:
        TypeError: If size is not an integer or position
        is not a tuple of 2 positive integers.
        ValueError: If size is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of each side of the square (default is 0).
            position (tuple): The position of the square in
            the x-axis and y-axis (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position
            is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        Adjusts position of the square according to specified position.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for x in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for z in range(self.__size):
                print("#", end="")
            print()

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

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: The position of the square in the x-axis and y-axis.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position value.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
