#!/usr/bin/python3

import math


class MagicClass:
    """
    This class represents a MagicClass with
    methods to calculate area and circumference.

    Attributes:
        __radius (float): The radius of the circle.
    """

    def __init__(self):
        """
        Initializes a new instance of the
        MagicClass with a default radius of 0.
        """
        self.__radius = 0

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The calculated area.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The calculated circumference.
        """
        return 2 * math.pi * self.__radius
