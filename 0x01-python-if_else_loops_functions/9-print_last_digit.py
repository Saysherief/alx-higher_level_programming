#!/usr/bin/python3
def print_last_digit(number):
    """
    Returns value of the last digit
    """
    last_dig = abs(number) % 10
    print("{}".format(last_dig), end="")
    return last_dig
