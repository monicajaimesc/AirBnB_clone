#!/usr/bin/python3
"""Model for test case is the individual unit of testing.
It checks for a specific response to a particular set of inputs.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test for Base Model"""
    
    @classmethod
    # setUpClass class method called before tests in an 
    # individual class run
    
 
    def setUpClass(cls):
        """
            defines all common attributes
            /methods for other classes:
        """
        cls.base1 = BaseModel()
        cls.base1.name = "Holberton"
        cls.base1.my_number = 89
        cls.base2 = BaseModel()
        cls.base2.name = "Betty"
        cls.base2.my_number = 98
        
    @classmethod
    def tearDownClass(cls):
        """
        class method called after tests in an individual class have run
        Tears down the instances
        """
        pass

    

    def test_docs(self):
        """Documentation of everithing"""
        # All your modules should have a documentation 
        self.assertTrue(BaseModel.__doc__)
        # All your classes should have a documentation
        self.assertTrue(BaseModel.save.__doc__)
        # All your functions (inside and outside a class)
        # should have a documentation
        self.assertTrue(BaseModel.to_dict.__doc__)
        
    def test_basic_functionality(self):
        """Test basic functionality of class"""
        # Test instance creation
        self.assertIsInstance(self.base1, BaseModel)
        # hasattr: Return whether the object has an 
        # attribute with the given name.
        self.assertTrue(hasattr(self.base1, "id"))
        # id != name 
        self.assertNotEqual(self.base1, self.base2)
        # when an instance is created
        # the time is update
        #self.assertEqual(self.base1.created_at,
        self.assertEqual(type(getattr(self.base1, 'created_at', None)), datetime)

        


if __name__ == '__main__':
    unittest.main()
