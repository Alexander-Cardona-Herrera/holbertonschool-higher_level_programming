#!/usr/bin/python3
"""
Defining the module.

Use this function wizely.
"""


class Student:
    """
    Class Student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        self.attrs = attrs
        
        if isinstance(attrs, list) == True:
            return self.__dict__

        return Student.__dict__
