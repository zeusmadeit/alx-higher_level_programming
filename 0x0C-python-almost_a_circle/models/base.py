#!/usr/bin/python3
"""Base Module containing the base class for this package"""
import json

class Base:
    """Base class for this package"""
    __nb_objects = 0

    def __init__(self, id=None): 
        if id != None: 
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return []
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None or len(list_objs) < 1:
            with open(f"{cls.__name__}.json", 'w') as fd:
                json.dump("[]", fd)
        else:
            n_list = []

            for index, el in enumerate(list_objs):
                n_list.append({k.replace(f"_{el.__class__.__name__}__", ""): getattr(el, k) for k in el.__dict__})

            strr = Base.to_json_string(n_list)

            with open(f"{cls.__name__}.json", 'w') as fd:
                fd.write(strr)
    