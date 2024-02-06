#!/usr/bin/python3
"""Module level documentation for from_json_string"""
import json

def from_json_string(my_str):
    """
    Function that returns an object (Python data structure) represented by a JSON string
    
    Args:
    my_str (string): json string to be deserialized

    Returns:
        object: pyhton object represented by the json string
    """
    return json.loads(my_str)