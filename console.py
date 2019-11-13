#!/usr/bin/python3
"""
Implementing the consola
"""

import cmd
import json
from models.base_model import BaseModel
import models
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
		Prints the string representation of 
  		an instance based on the class name and id.
		"""

		#of an instance based on the class name and id	
		args = args.split()
		# If the class name is missing  ** (ex: $ show)
		if len(args) == 0:
			print("** class name missing **")
			# If the class name doesn’t exist ** (ex: $ show MyModel)
		else:
			if args[0] in models.classes.keys():
				# [MyModel, ID]
				if len(args) >= 2:
					# all return all the object
					for key in models.storage.all().keys():
						# classname.id
						if key.split(".")[1] == args[1]:
							obj = all_objs[obj_id]
							print(obj)
							break
					else:
						# print, (ex: $ show BaseModel 121212)
						print("** no instance found **")
				else:
					print("print ** instance id missing **")
			else:
				print("** class doesn't exist **")
			
	def do_destroy(self, args):
		"""
		Deletes an instance based on the class name and id
		(save the change into the JSON file).
		"""
		
		args = args.split()
		if len(args) == 0:
			print('** class name missing **')
		else:
			# check if class exists
			if args[0] in models.classes.keys():
				# check if id was passed
				if len(args) >= 2:
					for key, value in models.storage.all().items():
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
    	"""
		
		args = args.split()
		# object list of strings
		object_list = []
		if len(args) == 0: 
			obj_dict = models.storage.all()
		if len(args) >= 2:
			obj_dict = models.storage.all(classes[args[0]])
			for key, value in models.storage.all().items():
				object_list.append(value.__str__())
				print(object_list)

		else:
			print("** class doesn't exist **")

			
		
		





if __name__ == "__main__":
	'''
		Entry point for the loop.
	'''
	HBNBCommand().cmdloop()




   