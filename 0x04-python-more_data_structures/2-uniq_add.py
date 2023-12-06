#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is None:
        return None
    uniq_int = set()
    for items in my_list:
        uniq_int.add(items)

    sum_uniq = sum(uniq_int)

    return sum_uniq
