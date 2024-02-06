#!/usr/bin/python3
"""describes function to appends string to text file"""


def append_write(filename="", text=""):
    """appends strings to text file"""
    with open(filename, 'a') as f:
        return f.write(text)
