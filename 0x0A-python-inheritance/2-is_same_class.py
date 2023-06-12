#!/usr/bin/python3
"""Method that checks whether the object is exactly an
instance of the specified class or not"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly
    an instance of the specified class ; otherwise False
    Args:
        obj: the object to be checked
        a_class: the class to compare to
    Returns:
        boolian according to the comparision
    """
    if type(obj) is a_class:
        return True
    else:
        return False
