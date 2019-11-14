#!/usr/bin/python3
""" Module tester to check if everything is working with User class """
import unittest
import pep8
from models.user import User
from models.base_model import BaseModel


class Test_user(unittest.TestCase):
    """ Tester to check if State is working as intended """

    def test_pep8(self):
        """
        it will check for pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "error pep8")

    def test_is_documented(self):
        """ checks for all documentation """
        self.assertIsNotNone(User.__doc__)

    def test_attribute(self):
        """ see if the attribute is the same"""
        my_user = User()
        my_user.name = "pony"
        self.assertEqual(type(my_user.name), str)

    def test_inheritance_from_clase(self):
        """ checks if the inherent is working well """
        my_user = User()
        self.assertTrue(issubclass(my_user.__class__, BaseModel), True)

    def test_docstring(self):
        """Check for docstrings"""
        self.assertIsNotNone(User.__doc__)
