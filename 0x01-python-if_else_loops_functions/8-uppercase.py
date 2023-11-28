#!/usr/bin/python3

def islower(c):

    return ord('a') <= ord(c) <= ord('z')


def uppercase(s):

    result = ""
    for char in s:
        result += "{}".format(chr(ord(char) - 32) if islower(char) else char)

    print(result)
