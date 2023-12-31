#!/usr/bin/python3
'''Module for the Rectangle class '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass of a rectangle '''
    def __init__(self, size):
        '''Initializes new square instance '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method calculates the area of square '''
        return self.__size ** 2
