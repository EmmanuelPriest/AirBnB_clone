#!/usr/bin/python3

'''Defines the class BaseModel'''
import models
import uuid import uuid4
from datetime import datetime


class BaseModel:
    '''Defines the Parent Model of the AirBnB_clone project'''

    def __init__(self, *args, **kwargs):
        '''Initializes the BaseModel

        Args:
            *args (any): Not used
            **kwargs (dict): Key/value pairs of attributes
        '''
        isotformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, isotformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        '''Update updated_at with the current time'''
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values of __dict__

        of the instance
        '''
        return_dict = self.__dict__.copy()
        return_dict["created_at"] = self.created_at.isoformat()
        return_dict["updated_at"] = self.updated_at.isoformat()
        return_dict["__class__"] = self.__class__.__name__
        return return_dict

    def __str__(self):
        '''Prints string representation of the BaseModel instances in

        this format: [<class name>] (<self.id>) <self.__dict__>
        '''
        temp = self.__class__.__name__
        return "[{}] ({}) {}".format(temp, self.id, self.__dict__)
