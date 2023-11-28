#!/usr/bin/python3
x = 'a'
while x <= 'z':
    print("{}".format(x), end="")
    x = chr(ord(x) + 1)
