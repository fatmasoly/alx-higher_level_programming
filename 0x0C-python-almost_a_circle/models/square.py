#!/usr/bin/python3
"""This Module for Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A subclass representing a square, derived from the Rectangle class.
    Attributes:
        size (int): The size of the square.
        x (int, optional): The x-coordinate of the square's position.
        y (int, optional): The y-coordinate of the square's position.
        id (int, optional): The id of the square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square object.

        Returns:
            str: A string representation of the Square object.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

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

        Args:
            value (int): The size to set for the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the properties of the square.

        Args:
            *args: Variable arguments. The first argument is
            the id, the second is the size,
                the third is the x-coordinate, and the
                fourth is the y-coordinate.
            **kwargs: Arbitrary keyword arguments.
            The valid keys are 'id', 'size', 'x', and 'y'.
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
        Convert the properties of the square object into a dictionary.

        Returns:
            dict: A dictionary representation of the square.
        """
        return {'id': self.id, 'x': self.x,
                'size': self.size, 'y': self.y}
