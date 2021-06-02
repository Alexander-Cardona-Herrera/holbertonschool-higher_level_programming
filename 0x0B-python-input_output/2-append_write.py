#!/usr/bin/python3
"""
For this function you have to put a file and a text as arguments.

Use this function wizely.
"""


def append_write(filename="", text=""):
    """
    Function that writes at the end of a file
    """
    with open(filename, mode="a+", encoding="UTF-8") as f:
        return f.write(text)
