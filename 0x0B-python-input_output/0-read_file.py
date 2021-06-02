#!/usr/bin/python3
"""
For this function you have to put a file as argument.

Use this function wizely.
"""


def read_file(filename=""):
    """
    Function that reads a file
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
    print()
