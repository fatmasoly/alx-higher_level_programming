#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_count = 0
    try:
        for n in range(x):
            print("{}".format(my_list[n]), end="")
            num_count += 1
    except (IndexError, TypeError):
        pass
    finally:
        print()
        return num_count
