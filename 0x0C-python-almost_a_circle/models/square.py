#!/usr/bin/python3
"""
Module description: This module defines the Square
class, a subclass of Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Summary: Square class, a subclass of Rectangle.

    Args:
        Rectangle (class): The base class for Square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the
            square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the
            square's position. Defaults to 0.
            id (int, optional): The id of the object. Defaults to None.

        Returns:
            Square: An instance of the Square class.
        """
        super.__init__(size, size, x, y, id)

        def __str__(self):
            """
            Return a string representation of the Square object.

        Returns:
            str: A string representation of the Square object.
            """
            return (f"[Square] ({self.id}) {self.x}/{self.y} - \
{self.height}")
        @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
            value (int): The new size of the square.

        Returns:
            None
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square object.

        Args:
            *args: Variable number of arguments (id, size, x, y).
            **kwargs: Variable number of keyword arguments.

        Returns:
            None
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if len(args) > 1:
            self.size = args[1]
        for k, v in kwargs.items():
            if k == "id" and v is not None:
                self.id = v
            elif k == "size" and v is not None:
                self.size = v
            elif k == "x" and v is not None:
                self.x = v
            elif k == "y" and v is not None:
                self.y = v

    def to_dictionary(self):
        """
        Convert the properties of the square
        object into a dictionary.

        Returns:
            dict: A dictionary representation of the square.
        """
        return {'id': self.id, 'x': self.x,
                'size': self.size, 'y': self.y}
