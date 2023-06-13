#!/usr/bin/python3
"""Method that checks whether the object is an instance of a class that
inherited (directly or indirectly) from the specified class or not"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False
    Args:
        obj: the object to be checked
        a_class: the class to compare to
    Returns:
        boolian according to the comparision
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
