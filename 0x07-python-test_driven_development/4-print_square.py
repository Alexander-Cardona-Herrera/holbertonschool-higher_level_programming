#!/usr/bin/python3
"""
For this function you can't use any type of characters bisides integers.

Only recive one argument.
"""


def print_square(size):
    """
    Print a square of # by the size.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        print("#" * size)
