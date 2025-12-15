#!/usr/bin/python3
"""Append CLI arguments to a JSON file."""
import sys

stjf = __import__('5-save_to_json_file')
lfjf = __import__('6-load_from_json_file')

try:
    args_list = lfjf.load_from_json_file("add_item.json")
except FileNotFoundError:
    args_list = []

args_list.extend(sys.argv[1:])
stjf.save_to_json_file(args_list, "add_item.json")
