#!/usr/bin/python3
"""
For this function you have to put an object and a class as arguments.

Use this function wizely.
"""


def inherits_from(obj, a_class):
    """
    Object of an instance.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
