#!/usr/bin/python3
"""
For this function you have to put a file as argument.

Use this function wizely.
"""


def read_file(filename=""):
    """
    Function that reads a file
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read())
