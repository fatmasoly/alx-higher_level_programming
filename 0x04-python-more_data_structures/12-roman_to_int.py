#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    a_dict = {'M': 1000,
              'D': 500,
              'C': 100,
              'L': 50,
              'X': 10,
              'V': 5,
              'I': 1}
    roman_string2 = []
    for x in range(len(roman_string)):
        if roman_string[x] in a_dict.keys():
            roman_string2.append(roman_string[x])
    add, sub = a_dict[roman_string2[-1]], 0
    for x in range(len(roman_string2) - 1):
        if a_dict[roman_string2[x]] < a_dict[roman_string2[x + 1]]:
            sub += a_dict[roman_string2[x]]
        else:
            add += a_dict[roman_string2[x]]
    return add - sub
