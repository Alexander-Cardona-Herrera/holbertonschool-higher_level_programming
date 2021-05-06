#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    alpha = sorted(a_dictionary.keys())

    for key in alpha:
        print(key, ':', a_dictionary[key])
