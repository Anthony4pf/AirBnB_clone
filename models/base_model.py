#!/usr/bin/env Python3
"""This module contains the BaseModel Class"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """Base Class that define common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Class Constructor"""

        if kwargs:
            for attr in kwargs.keys():
                if attr == '__class__':
                    continue
                elif attr == 'updated_at':
                    value = datetime.fromisoformat(kwargs['updated_at'])
                elif attr == 'created_at':
                    value = datetime.fromisoformat(kwargs['created_at'])
                else:
                    value = kwargs[attr]
                setattr(self, attr, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """String Representation of the Instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public attr updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dict containing keys/values of __dict__ of the instance"""
        new_dict = {**self.__dict__}
        new_dict.update({
                        "__class__": type(self).__name__,
                        "created_at": self.created_at.isoformat(),
                        "updated_at": self.updated_at.isoformat()})

        return new_dict
