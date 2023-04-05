#!/usr/bin/python3
"""Defines an integer addition function."""

def add_integer(a, b=98):
    """Adds two numbers
    Performs the addition between two numbers.
    Args:
        a (:obj:`int, float`): The first number.
        b (:obj:`int, float`, optional): The second number.
    Returns:
        int: The result of the addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer or float')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer or float')

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b


def convert_to_int(num):
    """Cast the data type of num parameter
    Convert a float number to an integer number
    Args:
        num (:obj:`int, float`): The number to cast.
    Returns:
        int: The number casted to integer.
    """
    if isinstance(num, float):
        num = int(num)
    return num

