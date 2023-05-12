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

    def test_kwargs_initialization(self):
        '''Test the initialization of a class using kwargs'''
        kwargs = {"__class__": "BaseModel",
                  "created_at": "2023-05-12T11:38:40.285816",
                  "updated_at": "2023-05-12T11:48:45.796947",
                  "id": "10089d3e-2fd7-4573-b219-bf027207e22e"
                  }
        Test_Base = BaseModel(**kwargs)
        self.assertEqual(Test_Base.id, kwargs['id'])
        self.assertEqual(Test_Base.created_at.isoformat(),
                         kwargs['created_at'])
        self.assertEqual(Test_Base.updated_at.isoformat(),
                         kwargs['updated_at'])


if __name__ == "__main__":
    unittest.main()
