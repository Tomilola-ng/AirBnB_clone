#!/usr/bin/python3
""" MY STORAGE SERIALIZING CODE """

import json

class FileStorage:
    """ CLASS FOR ADMIN FILE STORAGE """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all stored objects."""
        return self.__objects

    def new(self, obj):
        """Stores the object in the dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes the objects to the JSON file."""
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Deserializes the JSON file to objects."""
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass
