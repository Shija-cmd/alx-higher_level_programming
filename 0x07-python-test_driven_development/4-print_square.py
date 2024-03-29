#!/usr/bin/python3
"""
Name of a print_square
Printing a square with the character #.
"""


def print_square(size):
    """Printing a square where size is
    the length and width of the square.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        for m in range(size):
            print('#', end='')
        print()
