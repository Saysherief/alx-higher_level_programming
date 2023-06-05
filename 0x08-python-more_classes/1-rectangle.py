#!/usr/bin/python3
"""Define a class Rectangle"""

class Rectangle:
    """A class Rectangle that defines a rectangle

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
        """
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object

        Args:
            width: The width of the new rectangle, by default 0
            height: The height of the new rectanglee, default 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectanglee to value

        Args:
            value: the new width of the Rectangle

        Rasies:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectanglee to value

        Args:
            value: the new height of the Rectangle

        Rasies:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
