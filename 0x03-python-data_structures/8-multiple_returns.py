#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if not sentence:
        sentence = None
        return (leng, sentence)
    return (leng, sentence[0])
