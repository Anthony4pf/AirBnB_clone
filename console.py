#!/usr/bin/env python3
'''
module on AirBnB command line intepreter
'''
import cmd
from models.base_model import BaseModel
from models import storage

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
            all_objs = storage.all()
            key = command + "." + unique_id
            try:
                obj = all_objs[key]
                print(obj)
            except KeyError:
                print("** no instance found **")
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
