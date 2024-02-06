#!/usr/bin/python3
"""Modue level documentation"""

if __name__ == "__main__":
    import os.path
    import sys
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    my_arg = load_from_json_file('add_item.json') if os.path.isfile('./add_item.json') else []
    for i in enumerate(sys.argv):
        if (i[0] != 0):
            my_arg.append(i[1])
    save_to_json_file(my_arg, 'add_item.json')