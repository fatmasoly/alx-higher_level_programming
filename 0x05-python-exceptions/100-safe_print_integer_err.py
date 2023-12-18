#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="")
        return True
    except Exception as e:
        print("Exception:", e,  file=open("/dev/stderr", "w"))
        return False
