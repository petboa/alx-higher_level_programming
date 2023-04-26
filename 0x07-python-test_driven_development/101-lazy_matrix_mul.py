#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(a_c, a_d):
    """Return the multiplication of two matrices.
    Args:
        a_c (list of lists of ints/floats): The first matrix.
        a_d (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(a_c, a_d))
