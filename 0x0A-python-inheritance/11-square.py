#!/usr/bin/python3
'''Module for the Rectangle class '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Square subclass of Rectangle class '''
    def __init__(self, size):
        '''Initializes a new Square instance'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method Calculates and returns the area of the rectangle '''
        return self.__size ** 2

    def __str__(self):
        '''method Returns a string representation of the Rectangle '''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
