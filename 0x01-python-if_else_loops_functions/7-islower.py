#!/usr/bin/python3
def islower(c):
    """
    Returns True if c is lowercase or False otherwise
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
