#!/usr/bin/python3
""" BASE MODEL, in Which Every Model Inherits from. """

import uuid
import models
from datetime import datetime

class BaseModel:
    """ MOTHERBOARD :) SIMPLY GENERIC MODEL INSTANCE """

    def __init__(self, *args, **kwargs):
        """ Begin initialization """

        if kwargs:
            """ EDIT INSTANCE RATHER THAN CREATE NEW """
            self.__dict__.update(kwargs)
            if "created_at" in kwargs:
                self.created_at = datetime.fromisoformat(kwargs["created_at"])
            if "updated_at" in kwargs:
                self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            """ CREATEs NEW OBJECT ENTIRELY """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """  Rename default name """
        class_name = self.__class__.__name__
        return f'{class_name} {self.id} {self.__dict__}'

    def save(self):
        """ Updates the `updated_at` time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Working Smarter and presenting cleaner code """
        toDict = self.__dict__.copy()
        toDict["__class__"] = self.__class__.__name__
        toDict["created_at"] = self.created_at.isoformat()
        toDict["updated_at"] = self.updated_at.isoformat()
        return toDict
