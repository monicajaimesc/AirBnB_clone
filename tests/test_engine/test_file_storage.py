#!/usr/bin/python3
"""Unittest for FileStorage class
"""
import unittest
import pep8
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class file_Storage(unittest.TestCase):
    """Test for FileStorage"""

    @classmethod
    def setUpClass(cls):
        """
        defines all common attributes
        /methods for other classes:
        """
        cls.user = User()
        cls.user.email = "Holberton@school.com"
        cls.user.password = "password"
        cls.user.first_name = "Betty"
        cls.user.last_name = "Holberton"
        cls.stored = FileStorage()
    
    @classmethod
    def tearDownClass(cls):
        """
        class method called after tests in an individual class have run
        Tears down the instances
        """
        del cls.user
    
    def test_pep8(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "error pep8")

    def test_requeriments(self):
        """
        check if  all requeriments asked exist
        """
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "reload"))
        
    def test_docs(self):
        """Documentation of everithing"""
        # All your modules should have a documentation
        self.assertTrue(BaseModel.__doc__)
        # All your classes should have a documentation
        self.assertTrue(BaseModel.save.__doc__)
        # All your functions (inside and outside a class)
        # should have a documentation
        self.assertTrue(BaseModel.to_dict.__doc__)
        
    def test_all_method(self):
        """
        Tests that all gives the dict __object method
        """
        instances = self.stored.all()
        self.assertIsNotNone(instances)
        self.assertIsInstance(instances, dict)
        self.assertIs(instances, self.stored._FileStorage__objects)
    
    def test_new_method(self):
        """Tests that new sets a new object in __objects"""
        instances = self.stored.all()
        key = self.user.__class__.__name__ + "." + str(self.user.id)
        self.assertIsInstance(self.user, User)
        self.assertIsNotNone(instances[key])
    
    def reload_method(self):
        """Tests that reload deserializes the __objects from the JSON file"""
        my_us = User()
        my_us.name = "bonito pony"
        my_us.save()
        storage.save()
        storage.reload()
        storager = storage.all()
        self.assertIsNot(my_us, storager.values())

    