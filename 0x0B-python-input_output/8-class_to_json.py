#!/usr/bin/python3
"""
For this function you have to put an object  and a filename as arguments.

Use this function wizely.
"""


def class_to_json(obj):
    """
    Function that returns the JSON representation.
    """
    return obj.__dict__
