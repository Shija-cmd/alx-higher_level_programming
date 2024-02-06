#!/usr/bin/python3
"""describe a function to load from json file"""


def load_from_json_file(filename):
    """object from json file"""
    import json
    with open(filename, 'r') as f:
        return json.load(f)
