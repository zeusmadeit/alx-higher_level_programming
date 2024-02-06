#!/usr/bin/python3
"""Module level documentation for to_json_string"""
import json

def to_json_string(my_obj):
    """Function that returns the JSON representation of an object (string)

    Args:
    my_obj (object): a python object of any type

    Returns: the json representation of the object
    """
    str = json.dumps(my_obj, indent=4)
    return str
