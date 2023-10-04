#!/usr/bin/python3
"""
This is "0-add_integer" module
this module contains add_integers function that adds two integers
"""


def add_integer(a, b=98):
    """
    :param a: int or float
    :param b: int or float
    :return the sum of the two arguments
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
