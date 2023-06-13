#!/usr/bin/python3
"""Method that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)
    Args:
        my_obj: the objec to be represented
    Returns:
        JSON representation of the object
    """
    return json.dumps(my_obj)
