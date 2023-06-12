#!/usr/bin/python3
"""Method for listing available attributes and methods of an object"""


def lookup(obj):
    """
    function that returns the list of available attributes
    and methods of an object
    Args:
        obj: the object having attributes and methods
    Returns:
        list of available attributes and methods
    """
    return dir(obj)
