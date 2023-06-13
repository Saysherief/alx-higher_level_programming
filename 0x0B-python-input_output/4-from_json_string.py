#!/usr/bin/python3
"""Method that returns an object (Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string
    Args:
        my_str: the string that representes the object
    Returns:
        an object represented by the string
    """
    return json.loads(my_str)
