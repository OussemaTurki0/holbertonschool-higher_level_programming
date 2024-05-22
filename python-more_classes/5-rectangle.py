#!/usr/bin/python3
"""
Rectangle module
"""

class Rectangle:
    """
    Rectangle Class

    Attributes:
        width (int): Private
        height (int): Private
    """
    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle Class

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width getter

        Returns:
            int: The width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter

        Args:
            value (int): The value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height getter

        Returns:
            int: The height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter

        Args:
            value (int): The value to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Print the rectangle

        Returns:
            str: The rectangle represented by '#' characters
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (('#' * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """
        String representation of the rectangle

        Returns:
            str: The string representation of the rectangle
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message when an instance is deleted
        """
        print("Bye rectangle...")
