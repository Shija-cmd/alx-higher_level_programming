#!/usr/bin/python3
""" Importing json """

import json
""" Function to load from json file """

def load_from_json_file(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
