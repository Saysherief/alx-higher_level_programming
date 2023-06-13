#!/usr/bin/python3
"""Method that appends a string at the end of a text file (UTF8) and
returns the number of characters added"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    Args:
        filename: the name of the file to write into
        text: the content to be inserted in the file
    Returns:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        no_written = my_file.write(text)
        return no_written
