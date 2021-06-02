#!/usr/bin/python3
"""
defining the module.

Use this class wizely.
"""


class MyList(list):
    """
    Class Mylist.
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
