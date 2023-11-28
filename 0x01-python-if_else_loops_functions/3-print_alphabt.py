#!/usr/bin/python3

x = 'a'
while x <= 'z':
    if x == 'q' or x == 'e':
        x = chr(ord(x) + 1)
        continue
    print("{}".format(x), end="")
    x = chr(ord(x) + 1)
