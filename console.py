#!/usr/bin/python3
""" This is the console module"""

import cmd
import json
import re
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.review import Review

"""These are the imports"""

the_classes = {'BaseModel': BaseModel, 'User': User,
               'Amenity': Amenity, 'City': City, 'State': State,
               'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """ This defines the command interpreter
        Attribute:
                    prompt (str): The command prompt
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF(Ctrl-D)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Creates instance, save it and prints it with an id"""
        if arg == 0:
            print("** class name missing **")
        elif arg not in ['BaseModel', 'City', 'User', 'Place',
                         'Amenity', 'Review']:
            print("** class doesn't exist **")
        else:
            if arg == 'BaseModel':
                new_instance = BaseModel()
            elif arg == 'User':
                new_instance = User()
            elif arg == 'Place':
                new_instance = Place()
            elif arg == 'Amenity':
                new_instance = Amenity()
            elif arg == 'Review':
                new_instance = Review()
            elif arg == 'State':
                new_instance = State()
            elif arg == 'City':
                new_instance = City()
            new_instance.save()
            print(new_instance.id)
            storage.save()

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'State', 'City',
                             'User', 'Place', 'Amenity', 'Review']:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id is missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all().keys():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'User', 'State',
                             'Place' 'City', 'Amenity', 'Review']:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id is missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all().keys():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints string representation of all instances."""
        args = arg.split()
        if len(args) > 0 and args[0] not in the_classes.keys():
            print("** class doesn't exist **")
        else:
            inst_obj = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    inst_obj.append(obj.__str__())
                elif len(args) == 0:
                    inst_obj.append(obj.__str__())
            print(inst_obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute
        (save the change into the JSON file)"""

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ['BaseModel', 'User', 'State', 'Place',
                             'Amenity', 'Review', 'City']:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all().keys():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
