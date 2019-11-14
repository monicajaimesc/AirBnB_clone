#!/usr/bin/python3
"""Model for test case is the individual unit of testing.
It checks for a specific response to a particular set of inputs.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test for Base Model"""

    # setUpClass class method called before tests in an
    # individual class run
    @classmethod
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
        # self.assertEqual(self.base1.created_at,
        self.assertEqual(type(getattr(self.base1, 'created_at', None)),
                         datetime)

    def test_save(self):
        """
        Test if an instance can be saved
        """
        # instance saved
        self.base1.save()
        # instance created and time update
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_to_dict(self):
        """
        Test that a dictionary containing all keys/values of __dict__ of the
        instance that was returned
        """
        # acces to the instance dictionary
        # return all the keys values of __dict__
        # of the instance
        base1_dict = self.base1.to_dict()
        # is equal the class name
        self.assertEqual(self.base1.__class__.__name__, "BaseModel")
        # isinstance(a, b)
        self.assertIsInstance(base1_dict["created_at"], str)
        self.assertIsInstance(base1_dict["updated_at"], str)

if __name__ == '__main__':
    unittest.main()
