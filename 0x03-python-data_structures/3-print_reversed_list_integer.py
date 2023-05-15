#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    A function that prints all integers of a list in reverse
    """
    num = len(my_list) - 1
    if num >= 0:
        for i in range(num, -1, -1):
            print("{:d}".format(my_list[i]))
