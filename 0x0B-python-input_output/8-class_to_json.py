#!/usr/bin/python3
"""Method that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for
JSON serialization of an object"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data structure
    Args:
        obj: any of - list, dictionary, string, integer and boolean
    """
    return obj.__dict__
