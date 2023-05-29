#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    function that prints x elements of a list
    x represents the number of elements to print
    x can be bigger than the length of my_list
    Returns the real number of elements printed
    """
    printed = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed += 1
    except IndexError:
        pass
    print()
    return printed
