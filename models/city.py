#!/usr/bin/python3
"""module on a sub clas of Basemodel"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class that inherits from BaseModel"""
    name = ""
    state_id = ""
