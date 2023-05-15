#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    A function that prints a matrix of integers
    """
    for row in matrix:
        i = 0
        for num in row:
            print("{:d}".format(num), end="")
            if i == len(row) - 1:
                break
            print(end=" ")
            i += 1
        print()
