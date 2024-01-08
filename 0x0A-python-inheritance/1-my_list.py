#!/usr/bin/python3
"""
This module defines a class `MyList`.
"""


class MyList(list):
    """
    Customized list class that inherits from the built-in list class.

    Methods:
    - print_sorted(self)
        Prints the elements of the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.

        Parameters:
        - None

        Returns:
        - None
        """
        print(sorted(self))
