#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """
    A class Square that defines a square

    Attributes:
        __size: The size of the square (int)
        __position: The position of the square (tuple)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object

        Args:
            size: The size of the new square, by default 0
            posion: The position of the new square, default (0, 0)
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        get position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the Square to value

        Args:
            value: the new position of the Square
        Raises:
            TypeError: if position is not a tuple of 2 +ve integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or not isinstance
                (value[0], int) or not isinstance(value[1], int) or value[0]
                < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Prints the Square using no. of '#' as a size
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)
