#!/usr/bin/python3
'''Defines the FileStorage class.'''

import json
from models.base_model import BaseModel

class FileStorage:
    '''Definition of class FileStorage that handles serialization of instances
       to JSON file and deserialization of JSON files to instances
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    '''

    __file_path = "file.json"
    __objects = {}