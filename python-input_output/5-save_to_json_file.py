#!/usr/bin/python3
"""JSON file storage mocule."""
import json


def save_to_json_file(my_obj, filename):
    """Save an object to a file in JSON format."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
