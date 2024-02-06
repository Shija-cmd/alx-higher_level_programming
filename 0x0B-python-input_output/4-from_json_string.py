#!/usr/bin/python3
"""describes function to return object from JSON"""


def from_json_string(my_str):
    """returns object from json"""
    import json
    return json.loads(my_str)
