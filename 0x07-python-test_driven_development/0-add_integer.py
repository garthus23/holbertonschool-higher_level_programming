#!/usr/bin/python3


"""
    add_integer: add two integers
    Attributes: a(int): first int, b(int): second int
    Return: sum of a and b
"""


def add_integer(a, b=98):
    """
    function: add two integers
    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
