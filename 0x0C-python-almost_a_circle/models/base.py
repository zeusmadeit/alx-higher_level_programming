#!/usr/bin/python3
"""Base Module containing the base class for this package"""
import os.path
import json
import csv
import turtle

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
    
    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) < 1:
            return []
        else:
            return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        # create an instance of an existing class
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        list_inst = []
        if os.path.isfile(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json", "r") as fd:
                j_list = cls.from_json_string(fd.read())
                for obj in j_list:
                    list_inst.append(cls.create(**obj))

        return list_inst
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes data to CSV and saves it to file"""
        if list_objs is None or len(list_objs) < 1:
            with open(f"{cls.__name__}.csv", "w", newline="") as fd:
                fd.write("[]")
        else:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "width", "x", "y"]
            with open(f"{cls.__name__}.csv", "w", newline="") as fd:
                writer = csv.DictWriter(fd, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
    
    @classmethod
    def load_from_file_csv(cls):
        """loads and deserializes a CSV file"""

        if os.path.isfile(f"{cls.__name__}.csv"):
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "width", "x", "y"]

            with open(f"{cls.__name__}.csv", "r", newline="") as fd:
                csv_file = csv.DictReader(fd, fieldnames=fieldnames)

                list_dicts = [dict([k, int(v)] for k, v in row.items()) for row in csv_file]
                return [cls.create(**el) for el in list_dicts]

        return []

