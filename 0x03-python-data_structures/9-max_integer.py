#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    my_list.sort()
    length = len(my_list)
    return (my_list[length - 1])
