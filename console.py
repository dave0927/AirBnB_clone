#!/usr/bin/python3
'''The entry point of the command interpreter.'''

import cmd

class HBNBCommand(cmd.Cmd):
    '''HBNBCommand implements the Cmd class.
        It is a command  interpreter for the AirBnB project.

    Attributes:
            prompt (str): The command prompt.
    '''
    prompt = '(hbnb) '

    def do_quit(self, line):
        '''Quit command to exit the program.'''
        return True

    def do_EOF(self, line):
        '''EOF signal to exit the program.'''
        return True

    def emptyline(self):
        '''Do nothing when receiving an empty line.'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
