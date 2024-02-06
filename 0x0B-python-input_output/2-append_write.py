#!/usr/bin/python3
""" Function to append a file with utf-8
"""

def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
