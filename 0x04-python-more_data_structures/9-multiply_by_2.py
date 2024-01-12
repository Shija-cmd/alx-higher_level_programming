#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    my_dict = a_dictionary.copy()
    for key, value in my_dict.items():
        my_dict[key] = value * 2
    return my_dict
