#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None or len(sentence) == 0:
        length = 0
        first_char = None

    else:
        length = len(sentence)
        first_char = sentence[0]

    return length, first_char
