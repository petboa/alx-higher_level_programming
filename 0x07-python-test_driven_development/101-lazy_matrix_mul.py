#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def matrix_multiply(m_a, m_b):
    """Return the result of multiplying two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        A new matrix resulting from the multiplication of m_a and m_b.
    """

    return (np.matmul(m_a, m_b))
