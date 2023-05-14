#!usr/bin/python3
'''Define the BaseModel class'''

import uuid
import models
from datetime import datetime


class BaseModel():
    '''The base for all other classes in AirBnB project'''

    def __init__(self, *args, **kwargs):
        '''Initializes a new instance of the BaseModel class.
           Also recreate a class instance from a dictiornary.
        Attributes:
            id (str) - a unique identification number for each class instance
            created_at (datetime) - a datetime object indicating the date
                                    and time the instance was created
            updated_at (datetime) - a datetime object that is updated every
                                    time the instance object is modified
        '''

        time_format = '%Y-%m-%dT%H:%M:%S.%f'

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    time = datetime.strptime(value, time_format)
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''Return the string representation of the BaseModel instance'''
        clsname = self.__class__.__name__
        return ("[{}] ({}) {}".format(clsname, self.id, self.__dict__))

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
        new_dict.update({'created_at': self.created_at.isoformat()})
        new_dict.update({'updated_at': self.updated_at.isoformat()})
        new_dict.update({'__class__': self.__class__.__name__})
        return (new_dict)
