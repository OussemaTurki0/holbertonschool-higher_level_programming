#!/usr/bin/python3
"""
This module defines a Square class with size validation.
"""

class Square:
    """
    A class that defines a square.
    """
    def __init__(self, size=0):
        """
        Initialize the square with a private size attribute.
        Validate size to be an integer and >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
