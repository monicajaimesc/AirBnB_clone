#!/usr/bin/python3
"""
Module containing BaseModel class
"""
import uuid
from . import storage
from datetime import datetime


class BaseModel():
    """
    Defines all common attributes/methods for other classes. Parent class

    Attrs:
        id (string): unique id. assign with an uuid when an instance is created
        created_at (Date): current datetime when an instance is created
        updated_at (Date): current datetime when an instance is updated
    """

    def __init__(self, *args, **kwargs):
        """
        Method call when the instance is created
        Sets all atributes. Created_at and updated_at are datetime objs
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        storage.save()

    def to_dict(self):
        """
        Creates dictionary containing all keys/values of __dict__ of
        the instance.

        It converts the datetime objs into string object in ISO format
        using isoformat, then they are added to the dict

        Returns:
            (dict): dictionary with all instance attributes
        """

        # A copy was needed because we were not able to use storage.save()
        # This was due to __dict__ being edited by adding it __class__ key,
        # Also we were editing the value of updated_at and created_at keys
        # so when we were going to dump the obj it has a datetime obj as
        # value on updated_at key
        new_dict = self.__dict__.copy()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
