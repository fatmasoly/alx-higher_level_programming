#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="")
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=open("/dev/stderr", "w"))
        return False
