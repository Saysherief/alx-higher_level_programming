#!/usr/bin/python3
"""Method that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attribute, value):
    """
    function that adds a new attribute to an object if it’s possible
    Args:
        obj: the object having attributes and methods
        attribute: the attribute to be added
        value: value of the attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
