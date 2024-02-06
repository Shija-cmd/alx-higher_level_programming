#!/usr/bin/python3
"""describe function from class to json serialization"""


def class_to_json(obj):
    """returns dictionary description for json serialization"""
    return obj.__dict__
