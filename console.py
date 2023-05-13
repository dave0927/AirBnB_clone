#!/usr/bin/python3
'''The entry point of the command interpreter.'''

import cmd
import models
from models.base_model import BaseMode


class HBNBCommand(cmd.Cmd):
    '''HBNBCommand implements the Cmd class.
        It is a command  interpreter for the AirBnB project.

    Attributes:
            prompt (str): The command prompt.
    '''
    prompt = '(hbnb) '
