#!/usr/bin/python3
"""Define a class Base"""
import json


class Base:
    """
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all of my future classes
    and to avoid duplicating the same code

    Attributes:
        id (int): The id of the object
    """

    """private class attribute to keep track of no. of objects"""
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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Static method that returns the JSON string
        representation of list_dictionaries
        Args:
            list_dictionaries: is a list of dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        A class method that writes the JSON string
        representation of list_objs to a file:
        Args:
            cls: the class in which the object is instantiated
            list_objs: is a list of instances who inherits of Base
            example: list of Rectangle or list of Square instances
        '''
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as my_file:
            list_dictionaries = []
            for obj in list_objs:
                list_dictionaries += [obj.to_dictionary()]
            my_file.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        '''
        Static method that returns the list of the JSON string
        representation json_string:
        Args:
            json_string: a string representing a list of dictionaries
        '''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        A class method that returns an instance with all attributes already set
        Args:
            cls: the class itself
            dictionary: used as kwargs of the update method
        '''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
        Static method that opens a window and draws all the Rectangles and
        Squares
        Args:
            list_rectangles: list of instances rectangles
            list_squares: list of instances of squares
        '''
        t = turtle.Turtle()
        turtle.setup(width=600, height=300)
        turtle.setworldcoordinates(-300, -300, 300, 300)
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)
        turtle.done()
