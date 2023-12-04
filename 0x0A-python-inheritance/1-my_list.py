#!/usr/bin/python3
"""Module for looup method"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """a class MyList that inherits from list."""
        print(sorted(self))
