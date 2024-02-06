#!/usr/bin/python3
"""describes function to write string to text file"""


def write_file(filename="", text=""):
    """writes strings to text file"""
    with open(filename, 'w') as f:
        return f.write(text)
