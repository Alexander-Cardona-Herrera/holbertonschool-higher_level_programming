#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        a = len(sentence)
        b = sentence[0]
        tuple_a = (a, b)
    else:
        tuple_a = (0, None)
    return(tuple_a)
