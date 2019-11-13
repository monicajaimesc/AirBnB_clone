#!/usr/bin/python3
'''
    Package initializer
'''


from .engine.file_storage import FileStorage
from .base_model import BaseModel

# Dictionary that contain key and value
classes = {
    "BaseModel": BaseModel
}


storage = FileStorage()
storage.reload()

