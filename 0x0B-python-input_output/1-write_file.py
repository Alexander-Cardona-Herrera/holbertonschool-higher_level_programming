#!/usr/bin/python3
"""
For this function you have to put a file and a text as arguments.

Use this function wizely.
"""


def write_file(filename="", text=""):
    """
    Function that writes over a file
    """
    with open(filename, mode="w+", encoding="UTF-8") as f:
        return f.write(text)
