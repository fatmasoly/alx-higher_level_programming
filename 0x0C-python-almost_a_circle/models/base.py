#!/usr/bin/python3
"""
This module for the base class
"""
import json


class Base:
    """
    The base class for handling common functionality.

    Attributes:
        __nb_objects (int): A counter for the number of objects.
        id (int): The unique identifier for an object.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int, optional): The unique identifier
            Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: A JSON-formatted string.
        """
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): A JSON-formatted string.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to save.
        """
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f1:
            f1.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """
        Create an object from a dictionary.

        Args:
            **dictionary: Dictionary containing object attributes.

        Returns:
            object: An instance of the class.
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Load objects from a JSON file and create instances.

        Returns:
            list: List of created objects.
        """
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
