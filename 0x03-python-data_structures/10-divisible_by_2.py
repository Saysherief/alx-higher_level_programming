#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    A function that finds all multiples of 2 in a list
    """
    new_list = []
    for num in my_list:
        if (num % 2) == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
