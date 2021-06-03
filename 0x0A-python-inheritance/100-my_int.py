#!/usr/bin/python3
"""
defining the module.

Use this class wizely.
"""


class MyInt(int):
    """
    Class MyInt.
    """
    def __eq__(self, x: object):
        return super().__eq__(not x)

    def __ne__(self, x: object):
        return super().__ne__(not x)
