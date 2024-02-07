#!/usr/bin/python3
"""
================================
method is_same_class in module
================================
"""


def is_same_class(obj, a_class):
    """Method returning True if an object is an instance of a class"""

    return type(obj) is a_class
