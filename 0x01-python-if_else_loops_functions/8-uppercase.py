#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        if ord(str[x]) >= 97 and ord(str[x]) <= 122:
            y = ord(str[x]) - 32
        else:
            y = ord(str[x])
        print("{}".format(chr(y)), end='')
    print("")
