#!/usr/bin/python3
"""describe function to return json representatin of an object"""


def to_json_string(my_obj):
    """returns json representation of an object"""
    import json
    return json.dumps(my_obj, ensure_ascii=False)
