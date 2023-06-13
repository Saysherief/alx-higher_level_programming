#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """
    A class BaseGeometry that defines a Geometry
    """
    def area(self):
        """
        A function that returns the area of the Base Geometry
        Raises:
            Exception that it is not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A function that validates value
        Raises:
            TypeError and ValueError for non integer and negative
            integer respectively
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
