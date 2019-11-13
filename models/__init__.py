#!/usr/bin/python3
'''
    Package initializer
'''


from .engine.file_storage import FileStorage
from .base_model import BaseModel

# Dictionary that contain key and value
classes = {
    "BaseModel": BaseModel
    #"Amenity": Amenity
    #"City": City
    #"Place": Place
    #"Review": Review
    #"State": State
    #"User": User
}


storage = FileStorage()
storage.reload()

