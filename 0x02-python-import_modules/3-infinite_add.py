#!/usr/bin/python3
""" Importing sys

Auth: Juma Shija
"""
if __name__ == "__main__":
    import sys
    res = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            res += int(arg)
    print(res)
