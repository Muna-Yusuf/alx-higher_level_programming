#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        return (None)
    frist = sentence[0]
    return (leng, frist)
