#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """
    A list that inherits from list class
    """

    def __init__(self):
        """To initililize object"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
    
