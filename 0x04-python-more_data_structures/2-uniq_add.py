#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    function that adds all unique integers in a list only once for each integer
    """
    unique_set = set()
    for num in my_list:
        if isinstance(num, int):
            unique_set.add(num)
    answer = sum(unique_set)
    return answer
