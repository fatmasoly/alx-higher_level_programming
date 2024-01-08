#!/usr/bin/python3
'''Module for the MyInt subclass '''


class MyInt(int):
    """
    MyInt class inherits from int with == and != operators inverted.
    """

    def __eq__(self, other):
        """
        Override the == operator to invert its behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to invert its behavior.
        """
        return super().__eq__(other)
