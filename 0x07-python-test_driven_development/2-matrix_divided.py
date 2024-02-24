#!/usr/bin/python3
"""function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    Args:
        matrix: list of integers or floats

    Raises:
        TypeError exception
        Message matrix must be a matrix (list of lists) of integers/floats
        TypeError exception
        Message Each row of the matrix must have the same size
        TypeError exception
        Message div must be a number
        ZeroDivisionError exception
        Message division by zero
        TypeError
        Message matrix must be a matrix (array of arrays of integers/floats)

    Returns:
        new_matrix
    """
    
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of" +
                            " integers/floats")
        elif len(matrix[0]) != len(i) or len(matrix[0] == 0):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if isinstance(j, (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
    new_matrix = []
    new_matrix = [[round((j/div), 2) for j in i] for i in matrix]
    return new_matrix
