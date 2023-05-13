#!/usr/bin/env python3
'''
module on AirBnB command line intepreter
'''
import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    '''command line class'''

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """handles end of file"""
        print("")
        return True

    def emptyline(self):
        """Overrides the cmd empty line command"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return

        commands = line.split()
        command = commands[0]

        if command == "BaseModel":
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if not line:
            print("** class name missing **")
            return

        commands = line.split()
        if len(commands) < 2:
            print("** instance id missing **")
            return

        command, unique_id = commands[0], commands[1]

        if command == "BaseModel":
            storage.reload()
            all_objs = storage.all()
            key = command + "." + unique_id
            try:
                obj = all_objs[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroy an instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return

        commands = line.split()
        if len(commands) < 2:
            print("** instance id missing **")
            return

        command, unique_id = commands[0], commands[1]

        if command == "BaseModel":
            storage.reload()
            all_objs = storage.all()
            key = command + "." + unique_id
            try:
                del all_objs[key]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""

        storage.reload()
        all_objs = storage.all()
        list_objs = []

        if not line:
            for item in all_objs.values():
                list_objs.append(str(item))
            print(list_objs)
            return

        commands = line.split()
        class_name = commands[0]

        if class_name == "BaseModel":
            for key, value in all_objs.items():
                dict_objs = all_objs[key].to_dict()
                if dict_objs["__class__"] == "BaseModel":
                    list_objs.append(str(value))
            print(json.dumps(list_objs))
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return

        commands = line.split()

        if (len(commands) == 1):
            print("** instance id missing **")
            return
        if (len(commands) == 2):
            print("** attribute name missing **")
            return
        if (len(commands) == 3):
            print("** value missing **")
            return

        class_name = commands[0]
        u_id = commands[1]
        attr_name = commands[2]
        attr_value = commands[3]

        if class_name == "BaseModel":
            storage.reload()
            all_objs = storage.all()
            key = class_name + "." + u_id
            try:
                obj = all_objs[key]
            except KeyError:
                print("** no instance found **")
                return

            if hasattr(obj, attr_name):
                data_type = type(getattr(obj, attr_name))
                setattr(obj, attr_name, data_type(attr_value))
            else:
                setattr(obj, attr_name, attr_value)
            storage.save()
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
