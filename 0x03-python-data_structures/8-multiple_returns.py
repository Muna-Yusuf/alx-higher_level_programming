#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    leng = len(sentence)
    if leng <= 0:
        return (None)
    return (leng, sentence[0])
