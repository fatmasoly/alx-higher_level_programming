#!/usr/bin/python3
import sys
sum = 0
for args in range(len(sys.argv) - 1):
    sum += int(sys.argv[args + 1])
print(sum)
