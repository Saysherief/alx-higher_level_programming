#!/usr/bin/python3
def multiple_returns(sentence):
    """
    A function that returns a tuple with length of the string and its 1st char
    """
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
