#!/usr/bin/python3

def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return

    com_ele = set()
    for item in set_1:
        if item in set_2:
            com_ele.add(item)

    return com_ele
