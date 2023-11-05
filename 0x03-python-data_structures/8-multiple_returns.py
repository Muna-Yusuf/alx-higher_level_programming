#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if not sentence:
        sentence[0] = None
    if leng <= 0:
        return (None)
    return (leng, sentence[0])
