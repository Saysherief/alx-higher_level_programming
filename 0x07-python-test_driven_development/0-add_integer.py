#!/usr/bin/python3
'''A module which performes addition of two integers'''


def add_integer(a, b=98):
    """
    Returns an integer sum of a & b

    Args:
        a (int): must be an integer, must be casted to int if float
        b (int): must be an integer, must be casted to int if float
    Raises:
        TypeError: if a or b are not int or float
    """

    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
