#!/usr/bin/python3
"""Define an empty class Square"""


class Square:
    """
    A class Square that defines a square

    Attributes:
        __size: The size of the square
    """
    def __init__(self, new_size):
        """
        Initializes a new Square object

        Args:
            new_size: The size of the new square
        """
        self.__size = new_size
