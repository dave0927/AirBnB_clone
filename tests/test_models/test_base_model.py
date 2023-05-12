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

    def tearDown(self):
        '''Tear down the resources that had been setup to run tests'''
        del self.base_1
        del self.base_2

    def test_attributes_exist(self):
        '''Test that class BaseModel has the required methods and attributes'''
        self.assertTrue(hasattr(BaseModel, '__init__'))
        self.assertTrue(hasattr(self.base_1, 'id'))
        self.assertTrue(hasattr(self.base_1, 'created_at'))
        self.assertTrue(hasattr(self.base_1, 'updated_at'))
        self.assertTrue(hasattr(self.base_1, 'save'))
        self.assertTrue(hasattr(self.base_1, 'to_dict'))
        self.assertTrue(hasattr(BaseModel, '__str__'))

    def test_unique_IDs(self):
        '''Test that two instances of BaseModel class are assigned different unique IDs'''
        self.assertNotEqual(self.base_1.id, self.base_2.id)

if __name__ == "__main__":
    unittest.main()