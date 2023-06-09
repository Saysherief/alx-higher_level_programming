#!/usr/bin/python3
'''A module which prints My name is <first name> <last name>'''


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Args:
        first_name (str): must be a string
        last_name (str): must be a string
    Raises:
        TypeError: if either of the names are not strings
    """

    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
