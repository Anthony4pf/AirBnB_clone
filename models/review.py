#!/usr/bin/python3
"""module on a sub clas of Basemodel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reviewe class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
