#!/usr/bin/python3
"""Module for print_square mothod
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

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for x in range(size):
            print("#",end="")
        print()

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
