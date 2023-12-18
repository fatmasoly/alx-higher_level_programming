#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num_count = 0
    idx = 0

    try:
        for i in range(x):
            if idx >= x:
                print()
                return num_count
            try:
                print("{:d}".format(my_list[i]), end="")
                num_count += 1
            except (ValueError, TypeError):
                pass

        if idx < x:
            raise IndexError("list index out of range")

        print()
        return num_count
    except TypeError:
        return
