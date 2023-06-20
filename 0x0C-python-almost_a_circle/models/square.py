#!/usr/bin/python3
"""Defines a class Square which inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Base
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square object

        Args:
            size (int): The size of the new square
            x (int): The x coordinate of the top left corner of the square
            y (int): The y coordinate of the top left corner of the square
        """
        super().__init__(size, size, x, y, id)

    def area(self):
        """
        Returns area of the square
        """
        return self.width ** 2

    @property
    def size(self):
        """
        Gets the size/width of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size/width of the Square to value

        Args:
            value: the new width of the Square

        Rasies:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def display(self):
        '''
        Prints the rectangle according to the given dimention
        '''
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        '''
        String representation of the object
        '''
        str_val = "[Square] (" + str(self.id) + ") " + str(self.x) + "/"
        str_val += str(self.y) + " - " + str(self.size)
        return str_val
