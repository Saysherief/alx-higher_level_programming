#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase followed by a new line
    """
    for char in a str:
        if ord('a') <= ord(char) <= ord('z'):
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()
