#!/usr/bin/python3
"""defines a script that adds all arguments to a Python list,
    and then save them to a file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arlist = list(sys.argv[1:])

try:
    _data = load_from_json_file("add_item.json")
except Exception:
    _data = []

_data.extend(arlist)
save_to_json_file(_data, "add_item.json")
