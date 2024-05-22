#!/usr/bin/python3
"""
Module Devide Matrix
    """


def matrix_divided(matrix, div):
    """
    Devides all elements in matrix

    Args:
        matrix (list[list[int/float]]) : matrix
        div (int/float): Divider

    Raise:
        TypeError: div not int or float
        TypeError: matrix is not a list of lists of numbers
        ZeroDivisionError: div is 0

    Return : New matrix Divided
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    return [[round(num / div, 2) for num in row] for row in matrix]
