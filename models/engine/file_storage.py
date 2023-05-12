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

    def all(self):
        '''Return the dictionary __objects.'''
        return FileStorage.__objects
    
    def new(self, obj):
        '''Sets a new instance in the '__objects' dictionary using
           <obj class name>.id as the key

        Attributes:
            obj (object): object to be set in the __objects dictionary
        '''
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj