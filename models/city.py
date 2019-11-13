#!/usr/bin/python3
"""
Module that contains a class
City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class City that containts the attributes listed
    below
    Atributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """

    state_id = ""
    name = ""
