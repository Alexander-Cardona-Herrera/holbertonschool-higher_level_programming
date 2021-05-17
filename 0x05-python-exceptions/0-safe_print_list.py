#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if (my_list):
        try:
            for i in range(0, x):
                print("{}".format(my_list[i]), end='')

        except (IndexError):
            i = i - 1
            pass

        print("")
        return i + 1
