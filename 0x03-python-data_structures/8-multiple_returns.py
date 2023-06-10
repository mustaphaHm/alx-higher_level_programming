#!/usr/bin/python3
def multiple_returns(sentence):
    tupleS = 0, None
    if sentence != '':
        tupleS = len(sentence), sentence[0]
    return tupleS
