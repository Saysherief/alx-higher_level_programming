#!/usr/bin/python3
"""Method that checks whether the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class or not"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True if the object is an instance of, / if the object
    is an instance of a class that inherited from, the specified class;
    otherwise False
    Args:
        obj: the object to be checked
        a_class: the class to compare to
    Returns:
        boolian according to the comparision
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
