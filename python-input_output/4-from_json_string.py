#!/usr/bin/python3
"""JSON deserialization module."""

import json

def from_json_string(my_str):
    """Return an object from its JSON representation."""
    return json.loads(my_str)
