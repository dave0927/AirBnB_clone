#!/usr/bin/python3
'''Contains unittests for the BaseModel class methods'''

import unittest
from models.base_model import BaseModel

class TestBaseModelMethods(unittest.TestCase):
    '''Unittest test class for BaseModel class'''

    def setUp(self):
        '''Set up classes to be used to run the tests'''
        self.base_1 = BaseModel()
        self.base_2 = BaseModel()

if __name__ == "__main__":
    unittest.main()