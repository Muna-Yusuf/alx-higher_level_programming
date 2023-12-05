#!/usr/bin/python3
"""defines a JSON-to-object function"""


import json


def from_json_string(my_str):
    """Returns the python object representation of a JSON string"""
    return json.loads(my_str)
