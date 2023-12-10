#!/usr/bin/python3
""" creates the users model """

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel class
    but has it's own properties.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
