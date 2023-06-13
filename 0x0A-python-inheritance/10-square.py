#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        To initililize the object
        Args:
            size (int): size of the square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
