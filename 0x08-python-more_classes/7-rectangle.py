#!/usr/bin/python3
""" Authored by Krofah """

class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Width must be a non-negative integer.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Height must be a non-negative integer.")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        rect = ""
        for i in range(self._height):
            rect += "#" * self._width
            if i != self._height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        return f"Rectangle(width={self._width}, height={self._height})"


