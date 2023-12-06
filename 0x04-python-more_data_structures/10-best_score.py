#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_sco = {key: value * 2 for key, value in a_dictionary.items()}

    return best_sco
