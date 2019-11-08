#!/usr/bin/python3
"""
Module containing BaseModel class
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    Defines all common attributes/methods for other classes. Parent class

    Attrs:
        id (string): unique id. assign with an uuid when an instance is created
        created_at (Date): current datetime when an instance is created
        updated_at (Date): current datetime when an instance is updated
    """

    def __init__(self):
        """
        Method call when an instance is created
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Computes the "informal" string representations of an object
                Format: [<class name>] (<self.id>) <self.__dict__>
        Return:
            (str): formated string
        """
        string = "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        return string

    # Instance methods
    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        setattr(self, 'updated_at', datetime.now())

    def to_dict(self):
        """
        Creates dictionary containing all keys/values of __dict__ of
        the instance.

        It converts the datetime objs into string object in ISO format
        using isoformat, then they are added to the dict

        Returns:
            (dict): dictionary with all instance attributes
        """
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__
