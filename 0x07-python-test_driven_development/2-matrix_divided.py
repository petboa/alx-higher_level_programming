#!/usr/bin/python3
"""A module that divides all elements of a matrix of similar sized rows"""

def divide_matrix(matrix, divisor):
    """Returns a new matrix with each element divided by the divisor
    Args:
        matrix: a 2D array of integers/floats, each row should be the same size or else raises an error
        divisor: a non-zero number, otherwise raises an error
    Returns:
        a new matrix with each element adjusted to the divisor amount
    """
    error_message = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []

   if matrix is None or matrix == [[]]:
    raise TypeError(error_message)

if not isinstance(divisor, (int, float)) or divisor is None:
    raise TypeError("divisor must be a number")

if divisor == 0:
    raise ZeroDivisionError("division by zero")

matrix_size = len(matrix[0])
for row in matrix:
    if not isinstance(row, list):
        raise TypeError(error_message)

    if len(row) != matrix_size:
        raise TypeError("each row of the matrix must have the same size")

    new_row = []
    for element in row:
        if isinstance(element, (int, float)):
            new_row.append(round(element / divisor, 2))
        else:
            raise TypeError(error_message)
    new_matrix.append(new_row)

return new_matrix
