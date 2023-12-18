#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num_count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                num_count += 1
    except IndexError:
        raise IndexError("list index out of range")
    finally:
        print()
        return num_count
