#!/usr/bin/python3

for char in range(122, 96, -1):
    print("{:c}".format(char - 32 if char % 2 != 0 else char), end="")
print("")
