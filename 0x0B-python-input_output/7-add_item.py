#!/usr/bin/python3
"""Method that adds all arguments to a Python list, and then
saves them to a file"""
import sys
from os import path
save_to_jf = __import__("5-save_to_json_file").save_to_json_file
load_from_jf = __import__("6-load_from_json_file").load_from_json_file


def add_to_file(args, filename):
    """
    function that adds all arguments to a Python list
    then saves it to a file
    Args:
        args: arguments to be added to the file
        filename: text file to add to
    """

    if path.exists(filename):
        my_list = load_from_jf(filename)
    else:
        my_list = []
    my_list.extend(args)
    save_to_jf(my_list, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    add_to_file(args, "add_item.json")
