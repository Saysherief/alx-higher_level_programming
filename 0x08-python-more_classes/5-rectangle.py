#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle

    Attributes:
        width: The width of the rectangle (int)
        height: The height of the rectangle (int)
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle object

        Args:
            width: The width of the new rectangle, by default 0
            height: The height of the new rectanglee, default 0
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

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
        elif value < 0:
            raise ValueError("width must be >= 0")
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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def print(self):
        '''
        Prints the rectangle according to the given dimention
        '''
        if self.width == 0 or self.height == 0:
            print()
        else:
            for i in range(self.height):
                print("#" * self.width)

    def __str__(self):
        '''
        String representation of the object
        '''
        if self.width == 0 or self.height == 0:
            return ""
        else:
            str_val = ""
            for i in range(self.height):
                str_val += ("#" * self.width) + "\n"
            return str_val.rstrip("\n")

    def __repr__(self):
        '''
        Returns the string representation of the Rectangle for the developer
        '''
        str_val = "Rectangle(" + str(self.width) + ", "
        str_val += str(self.height) + ")"
        return (str_val)

    def __del__(self):
        '''
        Prints a delete message whenever an object of Rectangle is deleted
        '''
        print("Bye rectangle...")
