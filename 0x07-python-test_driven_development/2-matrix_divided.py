#!/usr/bin/python3
"""Module for add_integer mothod

   Function that divides all elements of a matrix.
   """


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.

       Args:
            matrix: A list of lists of integers or floats.
            div: The number that will be divided by the list.
       Raises:
            TypeError: If the list are not in (int, float).
            TypeError: If rows of the matrix are not the same size.
            TypeError: IF div are not in (int, float).
            ZeroDivisionError: If div == 0.
       Return: A new matrix.

    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
