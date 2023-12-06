#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None or search is None or replace is None:
        return my_list
    new_list = []
    for items in my_list:
        if items == search:
            new_list.append(replace)
        else:
            new_list.append(items)

    return new_list
