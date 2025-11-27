#!/usr/bin/python3
"""
Divide a matrix module
This module provides a function to divide a
matrix with multiple validation conducts
"""


def matrix_divided(matrix, div):
    """
    Divides each member of a matrix by the provided variable div

    Args:
        matrix: integer or float
        div: integer or float

    Returns:
        int/float: new matrix with all numbers from
        original matrix divided by div

    Raises:
        TypeError: if matrix is not a list of lists
        TypeError: if matrix is not made of integers/float
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            len(matrix) == 0):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            new_row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(new_row)

    return new_matrix
