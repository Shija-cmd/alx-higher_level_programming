#!/usr/bin/python3
"""Script to print from stdin"""
import sys

for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    print(d'File size: [{}]')
