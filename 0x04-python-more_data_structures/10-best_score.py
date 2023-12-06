#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

        a = a_dictionary.copy()
    for dic_key, dic_val in a.items():
        a[dic_key] *= 2
    return a
