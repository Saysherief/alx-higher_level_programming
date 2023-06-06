#!/usr/bin/python3
"""A function that prints a square with the character #"""


def print_square(size):
    """
    Prints the Square using no. of '#' as a size

    Args:
        size (int): the size of the Square

    Rasies:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
