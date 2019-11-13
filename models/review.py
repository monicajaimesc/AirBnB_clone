#!/usr/bin/python3
"""
Module that contains a class
Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review that containts the attributes listed
    below

    Atributes:
    place_id: empty string: it will be the Place.id
    user_id: empty string: it will be the User.id
    text: empty string
    """
    place_id = ""
    user_id = ""
    text = ""
