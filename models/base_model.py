#!usr/bin/python3
'''Define the BaseModel class'''

import uuid
from datetime import datetime
import models


class BaseModel():
    '''The base for all other classes in AirBnB project'''

    def __init__(self, **kwargs):
        '''nitialize a new instance of the BaseModel class.
           Also recreate a class instance from a dictiornary.
        Attributes:
            id (str) - a unique identification number for each class instance
            created_at (datetime) - a datetime object indicating the date
                                    and time the instance was created
            updated_at (datetime) - a datetime object that is updated every
                                    time the instance object is modified
        '''

        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        '''Return the string representation of the BaseModel instance'''
        cls_name = self.__class__.__name__
        return f"[{cls_name}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Update datetime after change'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all the relevant key/value pairs of
           an instance, including:
                - all key/value pairs from the __dict__ of the instance
                    - the created_at and updated_at attributes in string format
                      i.e (year-month-day T hour.minute.second.microsecond
                - a key __class__ whose value is the class of the instance
        '''
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
