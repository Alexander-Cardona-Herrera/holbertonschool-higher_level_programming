#!/usr/bin/python3
"""
For this function you have to put an object and a class as arguments.

Use this function wizely.
"""


def add_attribute(mc, name, new_instance):
    """
    Object of an instance.
    """

    if not hasattr(mc, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(mc, name, new_instance)
