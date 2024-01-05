#!/usr/bin/python3


class LockedClass:
    """
    A class with restricted attribute creation, allowing only 'first_name'.

    Attributes:
    __slots__ (list): A list specifying the allowed
    attribute names for instances of the class.
    """
    __slots__ = ['first_name']
