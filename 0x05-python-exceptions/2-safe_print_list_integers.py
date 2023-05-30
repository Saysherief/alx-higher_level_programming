#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    function that prints the first x elements of a list and only integers
    x represents the number of elements to print
    x can be bigger than the length of my_list
    Returns the real number of elements printed
    """
    printed = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed += 1
        print()
        return printed
    except IndexError:
        print()
        return printed
