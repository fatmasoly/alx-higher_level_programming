#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_sum = 0

    for args in range(len(sys.argv) - 1):
        total_sum += int(sys.argv[args + 1])

    print(total_sum)
