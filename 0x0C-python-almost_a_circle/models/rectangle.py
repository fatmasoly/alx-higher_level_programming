#!/usr/bin/python3
"""
This module defines the Rectangle class, which
represents rectangles with width, height, and position.
"""
from models.base import Base


class Rectangle(Base):
    """
    A class representing rectangles with properties
    for width, height, and position.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int, optional): The x-coordinate of the rectangle's position.
        y (int, optional): The y-coordinate of the rectangle's position.
        id (int, optional): The id of the object.
    """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Update the object's properties.

        Args:
            *args: Variable number of arguments (id, width, height, x, y).
            **kwargs: Variable number of keyword arguments.

        Returns:
            None
        """
        super().__init__(id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self, *args, **kwargs):
        """
        Update the object's properties.

        Args:
            *args: Variable number of arguments (id, width, height, x, y).
            **kwargs: Variable number of keyword arguments.

        Returns:
            None
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        for k, v in kwargs.items():
            if k == "id" and v is not None:
                self.id = v
            elif k == "width" and v is not None:
                self.width = v
            elif k == "height" and v is not None:
                self.height = v
            elif k == "x" and v is not None:
                self.x = v
            elif k == "y" and v is not None:
                self.y = v

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle's position.

        Parameters:
            value (int): The new y-coordinate.

        Returns:
            None

        Raises:
            TypeError: If the y-coordinate is not an integer.
            ValueError: If the y-coordinate is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle's position.

    Returns:
        int: The x-coordinate.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle's position.

    Parameters:
        value (int): The new x-coordinate.

    Returns:
        None

    Raises:
        TypeError: If the x-coordinate is not an integer.
        ValueError: If the x-coordinate is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def width(self):
        """
        Get the width of the rectangle.

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

    Returns:
        None

    Raises:
        TypeError: If the width is not an integer.
        ValueError: If the width is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

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

    Returns:
        None

    Raises:
        TypeError: If the height is not an integer.
        ValueError: If the height is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

    Returns:
        int: The area of the rectangle.
        """
        return self.width * self.height

    def __str__(self):
        """
        Return a string representation of the Rectangle object.

    Returns:
        str: A string representation of the Rectangle object.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def display(self):
        """
        Print a string representation of the rectangle.

    The rectangle is represented as a string of '#' characters,
    with one '#' character for each unit of width and height.
        """
        s = ""
        if self.height == 0 or self.width == 0:
            return s
        for a in range(self.y):
            s += "\n"
        for x in range(self.height):
            for b in range(self.x):
                s += " "
            for y in range(self.width):
                s += "#"
            if x != (self.height - 1):
                s += "\n"
        print(s)

    def to_dictionary(self):
        """
        Convert the properties of the rectangle
        object into a dictionary.

    Returns:
        dict: A dictionary representation of the rectangle.
        """
        return {'x': self.__x, 'y': self.__y,
                'id': self.id, 'height': self.__height, 'width': self.__width}
