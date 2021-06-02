#!/usr/bin/python3
"""
scrypt for appen elements.

Use this function wizely.
"""


import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    a = load_from_json_file("add_item.json")
except:
    a = []

for element in sys.argv[1:]:
    a.append(element)
save_to_json_file(a, "add_item.json")
