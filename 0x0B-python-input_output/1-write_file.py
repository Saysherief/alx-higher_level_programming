#!/usr/bin/python3
"""Method that writes a string to a text file (UTF8) and
returns the number of characters written"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    Args:
        filename: the name of the file to write into
        text: the content to be inserted in the file
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        no_written = my_file.write(text)
        return no_written
