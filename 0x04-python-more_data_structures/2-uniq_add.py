#!/usr/bin/python3

def uniq_add(my_list=[]):
    num_set = set(my_list)
    sum = 0
    for num in num_set:
        sum += num
    return sum
