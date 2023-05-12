#!/usr/bin/env python3
'''
module on AirBnB command line intepreter
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''command line class'''

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        '''handles end of file'''
        print()
        return True

    def emptyline(self):
        return cmd.Cmd.emptyline(self)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
