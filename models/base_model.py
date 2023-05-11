#!usr/bin/python3
'''Define the BaseModel class'''

import uuid
import models
from datetime import datetime


class BaseModel():
    '''The base for all other classes in AirBnB project'''

    def __init__(self, *args, **kwargs):
        '''Init a new base
            Args:
                *args: unlimited number of args
                **kwargs: dictionary based args
        '''

        time_format = '%Y-%m-%dT%H:%M:%S.%f'

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    time = datetime.strftime(value, time_format)
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # models.storage.new(self)
    
    def __str__(self):
        '''Return the string representation of the BaseModel instance'''
        return f'[{self.__class__.__name__} ({self.id} {self.__dict__})]'

    def save(self):
        '''Update datetime after change'''
        self.updated_at = datetime.now()