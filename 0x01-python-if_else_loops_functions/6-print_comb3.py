#!/usr/bin/python3
for a in range(0, 9):
    for b in range(0, 10):
        if a == b or a > b:
            continue
        if a == 8 and b == 9:
            continue
        print("{}{}, ".format(a, b), end='')
print("{}{}".format(a, b))
