#!/usr/bin/python3
"""JSON file loading module."""
import json


def load_from_json_file(filename):
    """Load an object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
