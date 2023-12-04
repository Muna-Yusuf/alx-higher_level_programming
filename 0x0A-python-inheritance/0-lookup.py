#!/usr/bin/python3
"""Module for looup method"""


def lookup(obj):
    """ function that returns the list of available
        attributes and methods of an object.

        Args:
            obj: to list the objects.

        Return:
            the list.
    """
    return (dir(obj))
