#!/usr/bin/python3

"""Module for add_integer mothod
    it adds 2 integers
    a and b must be first casted

    """


def add_integer(a, b=98):
    """Function Returns an integer: the addition of a and b
       Raises: TypeError: if a or b are not in (int, float).
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
