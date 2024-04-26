#!/usr/bin/python3
"""
This module defines a matrix division function
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a given number
    Args:
        matrix: A list of lists (matrix)- members can be of type ints or floats
        div: Number to be used for the division (can be a float or an integer)
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the divisions
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for rows in matrix:
        for ele in rows:
            if (not all(isinstance(ele, int) or not isinstance(ele, float))):
                raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        result.append(new_row)
    return result
