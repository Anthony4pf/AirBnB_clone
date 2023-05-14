#!/usr/bin/python3
"""module on a sub clas of Basemodel"""
from models.base_model import BaseModel


class Review(BaseModel):
	"""Reviewe class that inherits from BaseModel"""
	place_id = ''
	user_id = ''
	text = ''

    def __init__(self, *args, **kwargs):
        """Initialize a new User"""
        super().__init__(*args, **kwargs)
