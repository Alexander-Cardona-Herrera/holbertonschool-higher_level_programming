#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:

        up = (sum(i[0] * i[1] for i in my_list))
        down = (sum(i[1] for i in my_list))
        res = up / down
        return res
