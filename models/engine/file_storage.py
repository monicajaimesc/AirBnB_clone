#!/usr/bin/python3
"""
Declarates FileStorage class
"""
import json


class FileStorage:
    """
    will convert the dictionary representation to a JSON string.
    With this format, humans can read and all programming languages have a
    JSON reader and writer.

    Basically it will store the json to a file and deserialize
    that json to an obj, this way we restore all the data
    of the program. JSON files work as our database
    """

    def __init__(self):
        """
        Initialize instance with private attributes
        """
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """
        returns __object dictionary with all objs saved on file.json

        Returns:
            (dict): dictionary with all objs. Key of obj is "<class name>.id",
                    value is its .to_dict dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj.to_dict with key <obj class name>.id

        to_dict returns a dictionary that is already in a format
        that can be dump
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        Saves to a file the JSON representation of __objects dictionary
        """
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(self.__objects, file, indent="\t")

    def reload(self):
        """
        Converts the JSON string to a python obj
        and sets __objects with it
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                self.__objects = json.load(file)
        except Exception:
            pass
