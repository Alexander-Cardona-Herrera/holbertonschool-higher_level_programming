#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = 0
        for i in range(0, len(my_list) - 1):
            if max < my_list[i]:
                max = my_list[i]
            else:
                continue
    else:
        return(None)
    return(max)
