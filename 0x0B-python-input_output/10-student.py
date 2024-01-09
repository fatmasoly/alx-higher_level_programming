#!/usr/bin/python3
"""
This module about a class Student
"""


from attr import attrs


class Student:
    """
    A class Student that defines a student with attr: first_name, last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student object
        with the provided information.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        - attrs (list, optional): A list of strings representing attribute
        names to be included.If None, all attributes will be included.

        Returns:
        dict: A dictionary containing the selected
        attributes of the Student instance.
            """
            if not isinstance(attrs, list):
                return self.__dict__
        selected = {}
        for x in attrs:
            if not isinstance(x, str):
                return self.__dict__
            else:
                try:
                    selected[x] = self.__getattribute__(x)
                except AttributeError:
                    pass
        return selected
