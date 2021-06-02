#!/usr/bin/python3
"""
For this function you have to put an object and a class as arguments.

Use this function wizely.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Subclass Rectangle.
    """
    def __init__(self, width, height):
        self.__widht = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
