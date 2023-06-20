#!/usr/bin/python3
"""Defines a class Rectangle which inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
    A class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle object

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
            x (int): The x coordinate of the top left corner of the rectangle
            y (int): The y coordinate of the top left corner of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Returns area of the rectangle
        """
        return self.width * self.height

    @property
    def width(self):
        """
        Gets the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectanglee to value

        Args:
            value: the new width of the Rectangle

        Rasies:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Gets the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectanglee to value

        Args:
            value: the new height of the Rectangle

        Rasies:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Gets the x coordinate of the Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the x coordinate of the Rectanglee to value

        Args:
            value: the new coordinate of the Rectangle

        Rasies:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Gets the y coordinate of the Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y coordinate of the Rectanglee to value

        Args:
            value: the new coordinate of the Rectangle

        Rasies:
            TypeError: if value is not an integer
            ValueError: if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

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
        str_val = "[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/"
        str_val += str(self.y) + " - " + str(self.width) + "/"
        str_val += str(self.height)
        return str_val
