#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    leng = len(sentence)
    return (leng, sentence[0])
