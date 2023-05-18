#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    A function that prints a dictionary by ordered keys
    """
    sort_keys = sorted(a_dictionary.keys())
    for key in sort_keys:
        print(key, "\b:", a_dictionary[key])
