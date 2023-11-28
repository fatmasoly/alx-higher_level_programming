#!/usr/bin/python3

def islower(c):

    return ord('a') <= ord(c) <= ord('z')


def uppercase(s):

    for char in s:
        if islower(char):
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")

    print()
