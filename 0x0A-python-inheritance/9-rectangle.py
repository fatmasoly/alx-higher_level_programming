#!/usr/bin/python3
'''Module for the Rectangle class '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, a subclass of BaseGeometry"""
    def __init__(self, width, height):
        '''Constructor Initializes a new Rectangle instance'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Method Calculates and returns the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''method Returns a string representation of the Rectangle'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
