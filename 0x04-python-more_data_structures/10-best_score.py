#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val_max = 0
    key_max = None
    for key, value in a_dictionary.items():
        if value > val_max:
            val_max = value
            key_max = key
    return key_max
