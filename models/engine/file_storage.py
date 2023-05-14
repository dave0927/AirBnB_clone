#!/usr/bin/python3
'''Defines the FileStorage class.'''

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


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
        FileStorage.__objects[f"{ocname}.{obj.id}"] = obj

    def save(self):
        '''Serialize __objects to the JSON file __file_path.'''
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        try:
            with open(FileStorage.__file_path, "w") as f:
                json.dump(objdict, f)
        except Exception as e:
            print('Error while writting to file: ', e)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        -> Only IF it exists!
        """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass
