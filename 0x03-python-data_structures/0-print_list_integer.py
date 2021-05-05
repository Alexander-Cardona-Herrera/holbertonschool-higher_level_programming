#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        a = int(my_list[i])
        str = "{}"
        print(str.format(a))
