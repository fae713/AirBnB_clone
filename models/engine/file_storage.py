#!/usr/bin/python3
"""
    This is the FileStorage Module: This module
    defines a class that serializes instances to
    a JSON file and deserializes JSON file to instances.
"""
import json
import os
from model.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class File Storage:
    """ This is the FileStorage Class declaration
    Attributes:
                __file_path: Path to the JSON file
                __objects: Dictionary that stores all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This returns the dictionary __objects """

        return FileStorage.__objects

    def new(self, obj):
        """This sets in __objects the obj with key
        <obj class name>.id"""

        key = obj.__class__.__name__
        FileStorage.__object["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """ serializes __objects to JSON file
            (path: __file_path) """
        my_dict = FileStorage.__objects
        objdict = {}
        for obj in my_dict.keys():
            objdict[obj] = my_dict[obj].to_dict()
        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(objdict, f)

