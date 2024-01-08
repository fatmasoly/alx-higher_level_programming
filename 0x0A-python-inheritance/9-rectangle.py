#!/usr/bin/python3
'''This is module for Rectangle class '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class, a subclass of BaseGeometry.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Parameters:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator = ("width", width)
        self.integer_validator = ("height", height)

        def area(self):
            """
        Calculates and returns the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
            return self.__width * self.__height

        def __str__(self):
            """
        Returns a string representation of the Rectangle.

        Returns:
            str: String representation of the Rectangle.
        """
            return f"[Rectangle] {self.__width}/{self.__height}"
