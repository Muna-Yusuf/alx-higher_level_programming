#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
        return (None)
    leng = len(sentence)
    return (leng, sentence[0])
