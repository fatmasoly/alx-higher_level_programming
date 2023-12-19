#!/usr/bin/python3
""" this is the square module """


class Square:
    """ this is a square class """
    def __init__(self, size=0):
        """ this is the args
                size: first parameter.
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
