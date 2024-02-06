#!/usr/bin/python3
""" Importing json """

import json
""" Function to save to json file """

def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
