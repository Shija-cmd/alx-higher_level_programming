#!/usr/bin/python3
def roman_to_int(roman_string):
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    n = 0

    if type(roman_string) is str and roman_string:
        for j in range(len(roman_string) - 1, -1, -1):
            if value[roman_string[j]] >= n:
                result += value[roman_string[j]]
            else:
                result -= value[roman_string[j]]
            n = value[roman_string[j]]
    return result
