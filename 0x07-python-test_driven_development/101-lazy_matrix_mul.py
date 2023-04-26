#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        A new matrix resulting from the multiplication of m_a and m_b.
    """
    try:
        result = np.matmul(m_a, m_b)
    except ValueError as error:
        raise ValueError("Matrices cannot be multiplied: {}".format(error))
    except Exception as error:
        raise Exception("An error occurred while multiplying matrices: {}".format(error))
    return result

