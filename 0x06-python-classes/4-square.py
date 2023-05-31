#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """
    A class Square that defines a square

    Attributes:
        __size: The size of the square
    """
    def __init__(self, new_size=0):
        """
        Initializes a new Square object

        Args:
            new_size: The size of the new square, by default 0

        Raises:
            TypeError: if args is not an integer
            ValueError: if args is less than 0
        """
        if not isinstance(new_size, int):
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size

    def area(self):
        """
        Returns area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Gets the size of the Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the Square to value

        Args:
            value: the new size of the Square

        Rasies:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
