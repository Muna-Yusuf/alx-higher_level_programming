#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (None)
    x = tuple(sentence)
    leng = len(x)
    frist = x[0]
    return (leng, frist)
