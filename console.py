#!/usr/bin/python3
"""Defines the console"""

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the hbnb command interpreter"""

    prompt = "(hbnb) "

    def do_create(self, line):
        """Creates an instance.
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            cr = storage.classes()[line]()
            cr.save()
            print(cr.id)

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
