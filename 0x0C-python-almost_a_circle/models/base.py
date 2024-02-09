#!/usr/bin/python3
"""Base Module containing the base class for this package"""

class Base:
    """Base class for this package"""
    __nb_objects = 0

    def __init__(self, id=None): 
        if id != None: 
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects