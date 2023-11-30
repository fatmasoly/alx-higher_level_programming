#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argc))
        for n in range(argc):
            print("{}: {}".format(n + 1, sys.argv[n + 1]))
