#!/usr/bin/python3
"""This module conatins the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User"""
        super().__init__(*args, **kwargs)
