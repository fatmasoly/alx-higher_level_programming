#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    int_num = True
    try:
        print("{:d}".format(value), end="")
    except Exception as e:
        print("Exception:", e,  file=open("/dev/stderr", "w"))
        int_num = False
    return int_num
