#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers using a binary search"""


def find_peak(list_of_integers):
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    low_indx = 0
    high_indx = len(list_of_integers) - 1

    while low_indx < high_indx:
        mid_indx = (low_indx + high_indx) // 2
        if list_of_integers[mid_indx] < list_of_integers[mid_indx + 1]:
            low_indx = mid_indx + 1
        else:
            high_indx = mid_indx

    return list_of_integers[low_indx]
