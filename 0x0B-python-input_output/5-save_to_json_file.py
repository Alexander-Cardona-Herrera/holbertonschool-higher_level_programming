#!/usr/bin/python3
"""
For this function you have to put an object  and a filename as arguments.

Use this function wizely.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that returns the JSON representation.
    """
    with open(filename, "w+") as f:
        f.write(json.dumps(my_obj))
