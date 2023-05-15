#!/usr/bin/python3
def no_c(my_string):
    """
    A function that removes all characters c and C from a string
    """
    no_c_string = ''
    for char in my_string:
        if char not in 'cC':
            no_c_string += char
    return no_c_string
