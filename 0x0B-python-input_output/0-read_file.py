#!/usr/bin/python3
"""Method that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: the name of the file to read into
    """
    with open(filename, "r", encoding="utf-8") as my_file:
        print(my_file.read())
