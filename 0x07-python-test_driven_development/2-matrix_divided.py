#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix_list, divider):
    """Divides all elements of a matrix by divider.
    Args:
        matrix_list: list of lists containing int/ floats.
        divider: number to divide matrix by.
    Returns:
        List: list of lists containing divided matrix.
    Raises:
        TypeError: if matrix_list is not list of lists nor contains ints/ floats.
        TypeError: if sublists are not of the same size.
        TypeError: if divider is neither int nor float.
        ZeroDivisionError: when divider is zero.
    """
    if not isinstance(divider, (int, float)):
        raise TypeError("divider must be a number")
    if not isinstance(matrix_list, list) or len(matrix_list) == 0:
        raise TypeError("matrix_list must be a matrix (list of lists) of \
                        integers/floats.")

    for row in matrix_list:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix_list must be a matrix (list of lists) of \
                            integers/floats.")
        if len(row) != len(matrix_list[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix_list must be a matrix (list of lists) of \
                    integers/floats.")
    return [[round(x / divider, 2) for x in row] for row in matrix_list]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
