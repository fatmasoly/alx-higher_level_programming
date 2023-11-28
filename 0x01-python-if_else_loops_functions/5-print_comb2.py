#!/usr/bin/python3

x = 0
while x <= 99:
    print("{:02d}".format(x), end=", " if x < 99 else "\n")
    x += 1
