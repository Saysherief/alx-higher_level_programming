#!/usr/bin/python3
"""Method that writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that def save_to_json_file(my_obj, filename):
    Args:
        my_obj: the object to be saved into the file
        filename: text file to write to
    """

    with open(filename, "w") as my_file:
        json.dump(my_obj, my_file)
