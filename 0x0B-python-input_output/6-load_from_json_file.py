#!/usr/bin/python3
"""Doc string for module level documentation"""
import json

def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”

    Args:
    filename (file): file to load from

    Returns:
    object: python object
    """
    with open(filename, "r") as f:
        return json.load(f)
