#!/usr/bin/python3
"""
For this funtion you can't use any type of characters bisides int and float.

b is always initialized in 98 as default.
"""


def add_integer(a, b=98):
    """
    function that add two numbers of the type int or float and returns the add.
    """
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a + b)
