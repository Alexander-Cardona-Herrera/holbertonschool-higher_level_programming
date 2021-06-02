#!/usr/bin/python3
"""
For this function you have to put an object  and a filename as arguments.

Use this function wizely.
"""
import json


def load_from_json_file(filename):
    """
    Function that returns the JSON representation.
    """
    with open(filename, "r") as f:
        return json.load(f)
