#!/usr/bin/python3
"""
This module about a class Student
"""


class Student:
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

        def to_json(self):
            """
        Converts the Student object to a
        dictionary representation.

        Returns:
        dict: A dictionary containing the attributes
        of the Student object.
            """
            self.__dict__
