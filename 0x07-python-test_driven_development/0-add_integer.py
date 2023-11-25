#!/usr/bin/python3
"""Module for add_integer mothod"""


def add_integer(a, b=98):
    """Function Returns an integer: the addition of a and b

      Args:
            a: number 1.
            b: number 2.
       Raises:
            TypeError: if a or b are not in (int, float).
       Return: the sum of a and b.

    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


    if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
