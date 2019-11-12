#!/usr/bin/python3
"""
Implementing the consola
"""

import cmd


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
    

if __name__  ==  '__main__' : 
    """
        Entry point for the loop
    """
    HBNBCommand () . cmdloop ()

