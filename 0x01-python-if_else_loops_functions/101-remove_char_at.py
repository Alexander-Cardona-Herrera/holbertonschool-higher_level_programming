#!/usr/bin/python3
def remove_char_at(str, n):
    strcopy = ""
    for i in range(0, len(str)):
        if i == n:
            continue
        strcopy = strcopy + str[i]
    return(strcopy)
