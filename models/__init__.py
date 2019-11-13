#!/usr/bin/python3
'''
    Package initializer
'''


from .amenity import Amenity
from .base_model import BaseModel
from .city import City
from .engine.file_storage import FileStorage
from .place import Place
from .review import Review
from .state import State
from .user import User

# Dictionary that contain key and value
classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}

storage = FileStorage()
storage.reload()
