#!/usr/bin/python3
"""Module level documentation for save_to_json_file"""
import json

def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, 
    using a JSON representation

    Args:
    my_obj (object): a python object of any type
    filename (file): file to write to
    """
    return json.dump(my_obj, filename)
