#!/usr/bin/python3

def no_c(my_string):
    my_list = list(my_string)

    while 'c' in my_list:
        my_list.remove('c')

    while 'C' in my_list:
        my_list.remove('C')

    fin_string = ''.join(my_list)
    return fin_string
