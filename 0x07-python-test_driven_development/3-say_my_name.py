#!/usr/bin/python3
"""
For this funtion you can't use any type of characters bisides str.

last_name is empty by default.
"""


def say_my_name(first_name, last_name=""):
    """
    Print the string <first_name> and <last_name>.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
