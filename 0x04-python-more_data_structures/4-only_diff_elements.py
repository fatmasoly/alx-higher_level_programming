#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return

    a = set()
    for item in set_1:
        if item not in set_2:
            a.add(item)

            for item in set_2:
                if item not in set_1:
                    a.add(item)

    return a
