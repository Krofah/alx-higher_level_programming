#!/usr/bin/python3
"""
A module with a Rectangle that does nothing
"""

class Rectangle:
    """
    A class to represent a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle object with width and height
        """

        self._width = width
        self._height = height

    @property
    def width(self):
        """
        Returns the width of the rectangle
        """

        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self._width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle
        """

        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self._height = value

    def area(self):
        """
        Computes and returns the area of the rectangle
        """

        return self._width * self._height

    def perimeter(self):
        """
        Computes and returns the perimeter of the rectangle
        """

        return 2 * (self._width + self._height)

    def __str__(self):
        """
        Returns a string representation of the rectangle
        """

        return f"Rectangle({self._width}, {self._height})"

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        """

        return f"Rectangle({self._width}, {self._height})"

