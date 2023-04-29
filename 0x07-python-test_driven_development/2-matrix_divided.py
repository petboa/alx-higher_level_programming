#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix_list, divider):
    """Divides all elements of a matrix by divider.
    Args:
        matrix_list: list of lists containing integers/floats.
        divider: number to divide matrix by.
    Returns:
        List: list of lists containing divided matrix.
    Raises:
        TypeError: if matrix_list is not a list of lists or does not contain integers/floats.
        TypeError: if sublists are not of the same size.
        TypeError: if divider is not an int or float.
        ZeroDivisionError: when divider is zero.
    """
    if not isinstance(divider, (int, float)):
        raise TypeError("divider must be a number")
    if not isinstance(matrix_list, list) or len(matrix_list) == 0 or not all(isinstance(i, list) and all(isinstance(j, (int, float)) for j in i) for i in matrix_list):
        raise TypeError("matrix_list must be a matrix (list of lists) of integers/floats.")

    for row in matrix_list:
        if len(row) != len(matrix_list[0]):
            raise TypeError("Each row of the matrix must have the same size")
            
    return [[round(x / divider, 2) for x in row] for row in matrix_list]
        

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
