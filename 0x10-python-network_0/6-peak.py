#!/usr/bin/python3
"""Find a peak."""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers."""
    x = 0
    le = len(list_of_integers) - 1
    if list_of_integers:
        while x < le:
            mid = (x + le) // 2
            if list_of_integers[mid] > list_of_integers[mid + 1]:
                le = mid
            else:
                x = mid + 1
        return list_of_integers[x]
