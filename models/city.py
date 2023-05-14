#!/usr/bin/python3
"""module on a sub clas of Basemodel"""
from models.base_model import BaseModel


class City(BaseModel):
	"""city class that inherits from BaseModel"""
	name = ''
	state_id = ''

    def __init__(self, *args, **kwargs):
        """Initialize a new User"""
        super().__init__(*args, **kwargs)
