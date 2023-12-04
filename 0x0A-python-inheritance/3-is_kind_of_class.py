#!/usr/bin/python3
"""Defines a class-checking function."""


def is_kind_of_class(obj, a_class):
    """ a function that returns True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False

    Args:
        obj: to list the objects.
        a_class : The class to match the type of obj to.

    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
