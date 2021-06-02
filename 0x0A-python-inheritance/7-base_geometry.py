#!/usr/bin/python3
"""
For this function you have to put an object and a class as arguments.

Use this function wizely.
"""


class BaseGeometry:
    """
    class BaseGeometry.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
