#!/usr/bin/python3
"""
This module provide a class Student.
"""


class Student:
    """
    A class representing a student with attr: first_name, last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student object.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert the Student object's attributes into a dictionary.
        Args:
            attrs (list): attr list.

        Returns:
            dict: A dictionary representation of the Student object's attr.
        """
        if not isinstance(attrs, list):
            return self.__dict__
        ans = {}
        for x in attrs:
            if not isinstance(x, str):
                return self.__dict__
            else:
                try:
                    ans[x] = self.__getattribute__(x)
                except AttributeError:
                    pass
        return ans
