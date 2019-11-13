#!/usr/bin/python3
"""
Module that containg a FileStorage class
"""
import json
import models


class FileStorage:
	"""
	will convert the dictionary representation to a JSON string.
	With this format, humans can read and all programming languages have a
	JSON reader and writer.

	Basically it will store the json to a file and deserialize
	that json to an obj, this way we restore all the data
	of the program. JSON files work as our database
	"""

	__file_path = 'file.json'
	__objects = {}

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
		self.__objects[key] = obj

	def save(self):
		"""
		Saves to a file the JSON representation of __objects dictionary
		"""
		# open the file json and write it
		with open(self.__file_path, 'w', encoding="utf-8") as file:
			# create a new dictionary with the to_dict() method of the value (objects)
			dic_objects = {key:value.to_dict() for key, value in self.__objects.items()}
			json.dump(dic_objects, file, indent="\t")

	def reload(self):
		"""
		Converts the JSON string to a python obj
		and sets __objects with it
		"""
		try:
			with open(self.__file_path, 'r', encoding="utf-8") as file:
				json_objects = json.load(file)
				for key, value in json_objects.items():
					self.__objects[key] = models.BaseModel(**value)
		except Exception:
			pass
