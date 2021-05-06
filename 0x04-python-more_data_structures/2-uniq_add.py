#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        result = sum(set(my_list))
        return result
    else:
        return 0
