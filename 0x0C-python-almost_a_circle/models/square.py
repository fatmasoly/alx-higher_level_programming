#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A subclass representing a rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Rectangle object.

        Returns:
            str: A string representation of the Rectangle object
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - \
{self.height}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the object.

        Args:
            id (int, optional): The id of the object.
            size (int, optional): The width of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
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
