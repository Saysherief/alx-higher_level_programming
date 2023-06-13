#!/usr/bin/python3
"""Defines a class Myint that inherits from int"""


class MyInt(int):
    """
    A rebel that inherits from int class
    """

    def __eq__(self, value):
        """inverts == to !="""
        return super().__ne__(value)

    def __ne__(self, value):
        """inverts != to =="""
        return super().__eq__(value)
