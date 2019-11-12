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

        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = args.split()
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)
        
        except:
            print("** class doesn't exist **")
   
    def do_show(self, args):
        """
        Prints the string representation
        """ 
        #of an instance based on the class name and id
    
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
    
        if len(args) == 0:
            print("** class doesn't exist **")
        
        elif len(args) < 2:
            print()
        





if __name__ == "__main__":
    '''
        Entry point for the loop.
    '''
    HBNBCommand().cmdloop()




   