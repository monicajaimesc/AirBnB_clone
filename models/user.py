#!/usr/bin/python3
"""
Module that contains a class
User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User that containts the attributes listed
    below
    Atributes:
    email's user: empty string
    pasword's user: empty string
    first_name's user: empty string
    last_name's user: empty string
    """
    # public class attributes
    email = ""
    password = ""
    first_name = ""
    last_name = ""
