#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase followed by a new line
    """
    uppercase = ""
    for char in a str:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase += chr(ord(char) - 32)
        else:
            uppercase += char
    print("{}".format(uppercase))
