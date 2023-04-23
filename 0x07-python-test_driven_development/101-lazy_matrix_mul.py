#!/usr/bin/python3
"""A function that performs matrix multiplication using NumPy."""

import numpy as np


def multiply_matrices(m_a, m_b):
    """Multiply two matrices using NumPy.
    
    Arguments:
    m_a -- The first matrix.
    m_b -- The second matrix.
    
    Returns:
    The product of the two matrices.
    """
    return np.matmul(m_a, m_b)
