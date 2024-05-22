#!/usr/bin/python3
"""
Matrix Division Module
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of the matrix by a divisor

    Args:
        matrix (list of lists of int/float): 2D list with rows of equal size
        div (int/float): divisor

    Raises:
        TypeError: if matrix elements are not lists of integers/floats
        TypeError: if rows of matrix are not the same size
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div is zero

    Returns:
        list of lists: new matrix with each element divided by div and rounded to 2 decimal places
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(ele, (int, float)) for row in matrix for ele in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) for ele in row] for row in matrix]
