#!/usr/bin/python3

def islower(c):

    return ord('a') <= ord(c) <= ord('z')


def uppercase(s):

    for char in s:
        print("{}"
              .format(chr(ord(char) - 32) if islower(char) else char),
              end="")


print()
