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

    def update(self, *args, **kwargs):
        '''
        A public method that assigns an argument to each attribute
        1st: id
        2nd: size
        3rd: x
        4th: y
        Updated with kwargs that assigns a key/value argument to attributes
        '''
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        '''
        String representation of the object
        '''
        str_val = "[Square] (" + str(self.id) + ") " + str(self.x) + "/"
        str_val += str(self.y) + " - " + str(self.size)
        return str_val
