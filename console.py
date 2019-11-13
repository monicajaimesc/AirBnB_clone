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
		# If the class name is missing, 
		# print (ex: $ create)
		if len(args) == 0:
			print("** class name missing **")
		else:
			# args = BaseModel
			if args[0] in models.classes.keys():
				new_instance = eval(args[0])()
				new_instance.save()
				print(new_instance.id)
			else:
				print("** class doesn't exist **")
   
	def do_show(self, args):
		"""
		Prints the string representation
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




		





if __name__ == "__main__":
	'''
		Entry point for the loop.
	'''
	HBNBCommand().cmdloop()




   