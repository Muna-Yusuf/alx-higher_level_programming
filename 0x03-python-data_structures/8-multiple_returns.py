#!/usr/bin/python3
def multiple_returns(sentence):
    x = tuple(sentence)
    leng = len(x)
    if leng == 0:
        return (None)
    frist = x[0]
    return (leng, frist)
