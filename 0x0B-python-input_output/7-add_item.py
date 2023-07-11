#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
arguments = sys.argv[1:]
try:
    obj = load_from_json_file(file_name)
except FileNotFoundError:
    save_to_json_file([], file_name)

obj = load_from_json_file(file_name)
if type(obj) is list:
    for e in arguments:
        obj.append(e)

save_to_json_file(obj, file_name)
