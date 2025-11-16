#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    biggest = float('-inf')
    biggest_key = None

    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
            biggest_key = key
    return biggest_key
