#!/usr/bin/python3
"""Method that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”
    Args:
        filename: text file to load from
    """

    with open(filename, "r") as my_file:
        my_obj = json.load(my_file)
    return my_obj
