#!/usr/bin/python3
""" this is the square module """


class Square:
    """ a square class """
    def __init__(self, size=0):
        """ args : size
        TypeError:if size is not int
        ValueError:if size < 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area method to compute the area of the square

           Return:
               the area of the square.

           """
        return self.__size ** 2
