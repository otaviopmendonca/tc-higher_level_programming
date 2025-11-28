
#!/usr/bin/python3
"""
Lazy matrix multiplication module
This module provides a function to multiply two matrices using NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies m_a and m_b using NumPy

    Args:
        m_a: matrix a (float or integer)
        m_b: matrix b (float or integer)

    Returns:
        Result of matrix multiplication as a NumPy array
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for element in row:
            if not isinstance(element, (float, int)):
                raise TypeError("m_b should contain only integers or floats")

    a_cols = len(m_a[0])
    for row in m_a:
        if len(row) != a_cols:
            raise TypeError("each row of m_a must be of the same size")

    b_cols = len(m_b[0])
    for row in m_b:
        if len(row) != b_cols:
            raise TypeError("each row of m_b must be of the same size")

    if a_cols != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
