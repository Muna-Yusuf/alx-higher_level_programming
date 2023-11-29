#!/usr/bin/python3

""" Module for print_square mothod
   function that prints a square
   with the character #.

   """


def print_square(size):
    """a function that prints a square with the character #.

        Args:
            size: numbers of #.

        Raises:
            TypeError: If size is not int.
            TypeError: If size is float and less than 0.
            ValueError: If size is less than 0.

        Return:
            a square of size
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
