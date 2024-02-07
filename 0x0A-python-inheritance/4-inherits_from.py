#!/usr/bin/python3
"""
===================================
method inherited_from in module
===================================
"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
