#!/usr/bin/python3
"""Define a class Base"""


class Base:
    """
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all of my future classes
    and to avoid duplicating the same code

    Attributes:
        id (int): The id of the object
    """

    #private class attribute to keep track of no. of objects
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base object

        Args:
            id (int): The id of the object
        """
        if id is None: 
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
