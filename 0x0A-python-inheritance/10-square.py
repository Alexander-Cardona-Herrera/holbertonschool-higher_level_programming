#!/usr/bin/python3
"""
Defining the module.

Use this function wizely.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Subclass Square.
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return ("{}".format(self.__size * self.__size))

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
