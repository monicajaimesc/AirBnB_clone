#!/usr/bin/python3
"""
Implementing the consola
"""

import cmd
import json
from models.base_model import BaseModel
import models
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# base = {'BaseModel': Basemodel}

class HBNBCommand(cmd.Cmd):
	"""
	it cointains the entry point of the command interpreter
	"""

	prompt = ("(hbnb) ")

	def emptyline(self):
		"""
		empty line + ENTER shouldn’t 
		execute anything
		"""
		pass

	def do_quit(self, args):
		"""Quit command to quit the program
		"""
		return True
	
	def do_EOF(self, args):
		"""
			EOF command to end a file
		"""
		return True
	
	def do_create(self, args):
		"""
		Creates a new instance of BaseModel, saves it (to the JSON file)
		"""
		# create BaseModel
		
		args = args.split()
		# print(args)
		if len(args) == 0:
			print("** class name missing **")
		else:
			# args = [BaseModel]
			if args[0] in models.classes.keys():
				new_instance = eval(args[0])()
				new_instance.save()
				print(new_instance.id)
			else:
				print("** class doesn't exist **")

	def do_show(self, args):
		"""
		Prints the string representation of an instance 
  		based on the class name and id. 
    	
     	Ex: $ show BaseModel 1234-1234-1234.
		"""

		# tokenize args	
		args = shlex.split(args)
		# If the class name is missing or empty ** (ex: $ show)
		if len(args) == 0 or args[0] =="":
			print("** class name missing **")
		# If the class name doesn’t exist ** (ex: $ show MyModel)
		else:
			if args[0] in models.classes.keys():
				# [MyModel, ID]
				if len(args) > 1:
					# all return all the object
					key = args[0] + "." + args[1]
					if key in models.storage.all():
						print(models.storage.all()[key])
					else:
						# print, (ex: $ show BaseModel 121212)
						print("** no instance found **")
				else:
					print("** instance id missing **")
			else:
				print("** class doesn't exist **")
			
	def do_destroy(self, args):
		"""
		Deletes an instance based on the class name and id
		(save the change into the JSON file).
		"""
		
		# tokenize args
		args = args.split()
		if len(args) == 0:
			print('** class name missing **')
		else:
			# check if class exists
			if args[0] in models.classes.keys():
				# check if id was passed
				if len(args) > 1:
					for key in models.storage.all().keys():
						id_object = key.split('.')[1]
						if args[1] == id_object:
							del models.storage.all()[key]
							models.storage.save()
							break
					else:
						print("** no instance found **")
				else:
					print('** instance id missing **')
			else:
				print("** class doesn't exist **")
    
    
	def do_all(self, args):
		"""
		Prints all string representation of all 
		instances based or not on the class name

		Ex: $ all BaseModel or $ all
		"""

		args = shlex.split(args)
		# no matter class name is missing, storage it
		if len(args) == 0:
			objects = models.storage.all()
			# Create a new string object from the given object
			list_string = [str(objects[obj]) for obj in objects]
			# print list_string $all form
			print(list_string)

		# stoage when a class name exists
		elif len(args) > 0 and args[0] in models.classes.keys():
			objects2 = models.storage.all()
			list_string_name = [str(objects2[obj]) for obj in objects2 if args[0] in obj]
			# print $ all BaseMode form
			print(list_string_name)

		elif args[0] not in models.classes.keys():
			print("** class doesn't exist **")

	def do_update(self, args):
		"""
		Updates an instance based on the class name and id by adding
		or updating attribute (save the change into the JSON file).
		
		Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
		"""

		args = shlex.split(args)
		if len(args) == 0:
			print('** class name missing **')
		else:
			# check if class exists
			if args[0] in models.classes.keys():
				# check if id was passed
				if len(args) >= 2:
					# check if istance exists
					for key, value in models.storage.all().items():
						id_object = key.split('.')[1]
						if args[1] == id_object:
							instance = value
							# check if attribute name exists
							if len(args) >= 3:
								# check if attribute new value exists
								if len(args) >= 4:
									# get attribute type to cast new value
									try:
										attr_type = type(getattr(instance, args[2]))
										setattr(instance, args[2], attr_type(args[3]))
									except AttributeError:
										# if attribute does not exists then I set a new attribute
										# with the value passed
										setattr(instance, args[2], args[3])

									# Save changes
									models.storage.save()	
								else:
									print('** value missing **')
							else:
								print('** attribute name missing **')
							break
					else:
						print("** no instance found **")
				else:
					print('** instance id missing **')
			else:
				print("** class doesn't exist **")

	
			
		
		





if __name__ == "__main__":
	'''
		Entry point for the loop.
	'''
	HBNBCommand().cmdloop()




   
