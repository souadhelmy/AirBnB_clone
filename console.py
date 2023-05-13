#!/usr/bin/python3
"""This module defines a command interpreter class."""

import cmd
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from shlex import split

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '
    classes = [
        'BaseModel',
        'User',
        'State',
        'City',
        'Amenity',
        'Place',
        'Review'
    ]

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_create(self, args):
        """Create a new instance of a class."""
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        class_name = arg_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = models.classes[class_name]()
        models.storage.save()
        print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""

        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        class_name = arg_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        key = "{}.{}".format(class_name, instance_id)

        try:
            instance = models.storage.all()[key]
            print(instance)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return

        arg_list = args.split()
        class_name = arg_list[0]

        if class_name not in self.classes :
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance id missing **")
            return

        instance_id = arg_list[1]
        key = "{}.{}".format(class_name, instance_id)

        try:
            del models.storage.all()[key]
            models.storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name.
        """
        objects = models.storage.all()

        if not args:
            print([str(v) for v in objects.values()])
            return

        arg_list = args.split()
        class_name = arg_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        class_objects = [
            str(v) for v in objects.values() if type(v).__name__ == class_name
        ]
        print(class_objects)

    def do_update(self, args):
        """Update an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args_list[0], args_list[1])
        if key not in FileStorage().all():
            print("** no instance found **")
            return
        if len(args_list) < 3:
            print("** attribute name missing **")
            return
        if len(args_list) < 4:
            print("** value missing **")
            return
        instance = FileStorage().all()[key]
        attribute_name = args_list[2]
        if hasattr(instance, attribute_name):
            attribute_value = args_list[3]
            try:
                attribute_value = ast.literal_eval(attribute_value)
            except (ValueError, SyntaxError):
                pass
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        else:
            print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
    